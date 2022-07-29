from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
import json
from .models import User, Post
from django.views.decorators.csrf import csrf_exempt

class IndexView(generic.ListView):
    template_name = "network/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        """Return all posts in reverse chronological order"""
        return Post.objects.order_by("-timestamp")

def get_posts(request):

    posts = Post.objects.all().order_by("-timestamp")
    
    # return JsonResponse({'message': 'found get posts'})
    return JsonResponse([post.serialize() for post in posts], safe=False)


@csrf_exempt
@login_required
def make_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    if data.get("content") == "":
        return JsonResponse({"error": "Post must have content"}, status=400)
    
    new_post = Post(
        user=request.user,
        content=data.get("content")
    )
    new_post.save()

    return JsonResponse({"message": "Post made successfully."}, status=201)

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
