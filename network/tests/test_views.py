from urllib import response
from django.test import TestCase, Client
from network.models import User, Post
from django.urls import reverse

class ViewsTest(TestCase):

    def setUp(self) -> None:
        
        # Create Users
        User.objects.create_user('john', 'john@eagles.com', 'johnpassword').save()
        User.objects.create_user('paul', 'paul@eagles.com', 'paulpassword').save()

        # Get Users
        self.u1 = User.objects.get(username='john')
        self.u2 = User.objects.get(username='paul')


        # Create Post
        Post.objects.create(user=self.u1, content='Test contents').save()
    
    def test_make_new_valid_post(self):
        self.client.login(username='john', password='johnpassword')
        content = {'content' : 'Lorem Ipsum'}
        response = self.client.post(reverse('index'), content)
        self.assertEqual(response.status_code, 200)
        
    def test_make_new_invalid_post(self):
        self.client.login(username='john', password='johnpassword')
        content = {'content' : ''}
        response = self.client.post(reverse('index'), content)
        self.assertEqual(response.status_code, 400)
    
    def test_valid_post_update(self):
        self.client.login(username='john', password='jognpassword')
        post = Post.objects.get(user=self.u1)
        content = {'content': 'Lorem Ipsum'}
        response = self.client.put(reverse('update_post', args=(post.id,)), content, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_invalid_post_update(self):
        self.client.login(username='john', password='johnpassword')
        post = Post.objects.get(user=self.u1)
        content = {'content': ''}
        response = self.client.put(reverse('update_post', args=(post.id,)), content, content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_user_post_update_on_other_users_post(self):
        c = Client()
        c.login(username='paul', password='paulpassword')
        response = c.get(reverse('index'))
        print('##################')
        print(response.context['user'].id)
        print('##################')
        post = Post.objects.get(user=self.u1)
        content = {'content': 'Lorem Ipsum'}
        # response = self.client.put(reverse('update_post', args=(post.id,)), content, content_type='application/json')