from django.test import TestCase
from .models import User, UserFollowing

# Create your tests here.

class FollowTestCase(TestCase):
    def setUp(self) -> None:
        
        # Create Users
        u1 = User.objects.create_user('john')
        u2 = User.objects.create_user('paul')
        
        # Create UserFollowing

        # valid
        f1 = UserFollowing.objects.create(user=u1, following_user=u2)
        # invalid
        f2 = UserFollowing.objects.create(user=u1, following_user=u1)
    
    def test_valid_user_following(self):
        u1 = User.objects.get(username='john')
        u2 = User.objects.get(username='paul')
        f1 = UserFollowing.objects.get(user=u1, following_user=u2)
        self.assertTrue(f1.is_valid_follow())

    def test_invalid_user_following(self):
        u1 = User.objects.get(username='john')
        f1 = UserFollowing.objects.get(user=u1, following_user=u1)
        self.assertFalse(f1.is_valid_follow())