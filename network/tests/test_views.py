from django.test import TestCase
from network.models import User, Post
from django.urls import reverse

class ViewsTest(TestCase):

    def setUp(self) -> None:
        
        # Create Users
        User.objects.create_user('john', 'john@eagles.com', 'johnpassword').save()

        # Get Users
        self.u1 = User.objects.get(username='john')

        # Create Post
        Post.objects.create(user=self.u1, content="Test contents").save()
    
    def test_make_new_post(self):
        self.client.login(username='john', password='johnpassword')
        content = {"content" : ''}
        response = self.client.post(reverse('index'), content)
        # sent_post = Post.objects.get(user=self.u1, content='Lorem Ipsum')
        # self.assertEqual(content['content'], sent_post.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains