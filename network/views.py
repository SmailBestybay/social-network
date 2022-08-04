from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import User, Post
from django.core.paginator import Paginator
import json
from django.views.decorators.csrf import csrf_exempt

def index_view(request):

    posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts' : posts, 'page_obj' : page_obj}

    if request.method == 'POST':
        if request.POST['content'].strip() == '':
            context['message'] = 'Post must not be empty'
            return render(request, 'network/index.html', context, status=400)
        
        new_post = Post(
            user=request.user,
            content=request.POST['content']
        )
        new_post.save()

        return render(request, 'network/index.html', context)
            
    return render(request, 'network/index.html', context)

def profile_view(request):
    user = request.user

    posts = Post.objects.all().filter(user=user).order_by('-timestamp')
    paginator = Paginator(posts, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts' : posts, 'page_obj' : page_obj}

    return render(request, 'network/profile.html', context)

@csrf_exempt
def update_post(request, post_id):
    if request.method != "PUT":
        return JsonResponse({'error': "Put request required"}, status=400)
    
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    data = json.loads(request.body)
    if data["content"] == '':
        return JsonResponse({'error': 'Post must not be empty'}, status=400)
    
    if post.user != request.user:
        return JsonResponse({'error': "Can not edit other user's posts"}, status=400)
        
    post.content = data['content']
    post.save()
    return JsonResponse({'message': "put success"})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
