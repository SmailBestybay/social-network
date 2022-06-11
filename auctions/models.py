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
    # category of listing (eg. Toysm Fashion, Electronics)
    pass

class Bid():
    pass

class Comment():
    pass
