from django.contrib import admin
from .models import User, Post, UserFollowing

# Register your models here.
admin.site.register(User)
admin.site.register(UserFollowing)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'likes')