from django.test import TestCase
from myapp.models import Post, User

class TestAppModels(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title='Django Testing')
        content = Post.objects.create(content='This is some content')
        self.assertEqual(str(title), 'Django Testing')
    
    def test_user(self):
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username='testuser2', password='12345')
        title = Post.objects.create(
            title='Django', content='New Content')
        title.likes.set([testuser.pk, testuser2.pk])
        self.assertEqual(title.likes.count(), 2)



