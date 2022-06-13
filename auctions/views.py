from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import User, Listing
from .formhelper import NewListingForm

def index(request):
    # active listings should display
    # title, description, starting bid, current price, photo(if exists)
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
        })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# @login_required
def create_listing(request):
    # form to create a new listing must have fields:
    # title (must be filled)
    # description (must be filled)
    # starting bid (must be filled)
    # URL for an image
    # category
    # submit takes to newly created listing
    return render(request, "auctions/create_listing.html", {
        "NewListingForm" : NewListingForm()
    })

def listing(request, listing_id):
    # Display all details
    # include current price
    # if signed in, able to add item to "Watchlist"
    # if in "Watchlist", able to remove item
    # if signed it, able to bit on item 
    # bit must be >= starting bit and > all other bids, else error
    # if signed it and creator, able to close bid
    # if closed, make highest bidder the winner
    # if closed, make listing not active
    # if signed in on closed listing, display if user won.
    # diaplay comments
    # if signed in, able to add comments

    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing" : listing
    })

# @login_required
def watchlist(request):
    # display signed in user's watchlist
    # each item in list links to listing
    # able to remove from watchlist
    pass

def categories(request):
    # Display list of categories
    # item in list is link to list of active listings in category
    pass