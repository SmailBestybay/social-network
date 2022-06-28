from django.contrib import admin
from .models import User, Listing, Bid, Watchlist, Comment

# Register your models here.
# site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site
# HINT 
#To create a superuser account that can access Django’s admin interface, run python manage.py createsuperuser.

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comment)