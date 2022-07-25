from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self) -> str:
        return f"{self.username}"

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"User: {self.user}, Short Content: {self.content[:20]}..."

class UserFollowing(models.Model):
    """ Don't forget to block from following the same user twice """

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following")
    following_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="followers")

    def __str__(self) -> str:
        return f"{self.user} is following {self.following_user}"
    
    def is_valid_follow(self) -> bool:
        return self.user != self.following_user