from django.test import TestCase, Client
from .models import User, Post, UserFollowing
from django.urls import reverse
import json
from django.forms.models import model_to_dict

# Create your tests here.
# https://www.youtube.com/watch?v=hA_VxnxCHbo&ab_channel=TheDumbfounds
# https://docs.djangoproject.com/en/4.0/topics/testing/tools/


class NetworkTestCase(TestCase):
    
    def setUp(self) -> None:
        
        # Create Users
        User.objects.create_user('john', 'john@eagles.com', 'johnpassword').save()
        User.objects.create_user('paul', 'paul@eagles.com', 'paulpassword').save()
        
        # Get Users
        self.u1 = User.objects.get(username='john')
        self.u2 = User.objects.get(username='paul')

        # Create Post
        Post.objects.create(user=self.u1, content="Test contents").save()

        # Create valid and invalid UserFollowing
        UserFollowing.objects.create(user=self.u1, following_user=self.u2)
        UserFollowing.objects.create(user=self.u1, following_user=self.u1)


    def test_valid_user_following(self):
        f1 = UserFollowing.objects.get(user=self.u1, following_user=self.u2)
        self.assertTrue(f1.is_valid_follow())

    def test_invalid_user_following(self):
        f1 = UserFollowing.objects.get(user=self.u1, following_user=self.u1)
        self.assertFalse(f1.is_valid_follow())

    def test_valid_post_like_count(self):
        p1 = Post.objects.get(user=self.u1)
        self.assertGreaterEqual(p1.likes, 0)

    def test_invalid_post_like_count(self):
        p1 = Post.objects.get(user=self.u1)
        p1.likes = -1
        self.assertLess(p1.likes, 0)

    def test_make_post(self):
        dict_user = model_to_dict(self.u1)
        response = self.client.post(reverse('make_post'), json.dumps({
            'user': dict_user,
            'content': 'Lorem Ipsum'
        }))
        self.assertEqual(response.status_code, 201)

