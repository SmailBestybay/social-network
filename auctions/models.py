from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    
    # bids manny to many field as one user can have many bids
    # bids = models.ManyToManyField(Bid, blank=True, related_name="")
    # listings many to many relationship as a user can have many listings

    def __str__(self):
        return f"{self.username} "

class Listing(models.Model):
    # Listing needs to have:
    # id is set automatically
    # title not null
    title = models.CharField(max_length=64)
    # description not null
    description = models.CharField(max_length=64)
    # starting bid number not null
    starting_bid = models.IntegerField(validators=[MinValueValidator(0)])
    # URL for an image
    image = models.URLField(blank=True)
    # category of listing (eg. Toys, Fashion, Electronics)
    category = models.CharField(max_length=64, blank=True)
    # active boolean not null
    active = models.BooleanField(default=True)
    # creator user key AKA owner of the listing, related name returns all users that have listings
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sellers")
    # winner, user that has won the listing, related name should return all bids won by user
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_won", null=True, blank=True)


    def __str__(self):
        return f"{self.id}: {self.title}"

class Bid(models.Model):
    # id - auto create
    # user key - each bid belongs to a user, related name will return all users that have a bid AKA bidders.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidders")
    # listing key, every bid is joined to a listing, related name should return all listings that have bids 
    listing_key = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="have_bids")
    # bid ammount
    bid_amount = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.id}: {self.bid_amount}"

# class Comment(models.Model):
#     # id
#     # listing key
#     # user key
#     # time
#     # content
#     pass

# class Watchlist(models.Model):
#     # id
#     # user key
#     # listing key
#     pass