from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing():
    # Listing needs to have:
    # id
    # title not null
    # description not null
    # starting bid number not null
    # URL for an image
    # category of listing (eg. Toys, Fashion, Electronics)
    # creator user key
    # active boolean not null
    pass

class Bid():
    # id
    # user key
    # listing key
    # bit ammount
    pass

class Comment():
    # id
    # listing key
    # user key
    # time
    # content
    pass

class Watchlist():
    # id
    # user key
    # listing key
    pass