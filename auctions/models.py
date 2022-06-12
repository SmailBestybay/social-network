from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    # Listing needs to have:
    # id is set automatically
    # title not null
    title = models.CharField(max_length=64)
    # description not null
    description  = models.CharField(max_length=64)
    # starting bid number not null
    starting_bid = models.IntegerField()
    # URL for an image
    imgage = models.URLField(blank=True)
    # category of listing (eg. Toys, Fashion, Electronics)
    category = models.CharField(max_length=64, blank=True)
    # active boolean not null
    active = models.BooleanField()
    # creator user key


    def __str__(self):
        return f"{self.id}: {self.title}"

# class Bid(models.Model):
#     # id
#     # user key
#     # listing key
#     # bit ammount
#     pass

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