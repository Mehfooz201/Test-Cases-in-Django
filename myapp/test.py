from django.test import TestCase
from .models import BlogCategory

class urlTest(TestCase):

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    

class ModelTest(TestCase):
    def test_blog_category(self):
        categories = ['abc', 'xyz']
        for category in categories:
            obj = BlogCategory.objects.create(
                category_name = category
            )
            self.assertEquals(category, obj.category_name)
        
        objs = BlogCategory.objects.all()

        self.assertEqual(objs.count(), 2)