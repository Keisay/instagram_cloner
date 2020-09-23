from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from ..forms import NewPostForm

from post.models import Post

class TestPostForm(TestCase):
    def test_valid_form(self):
        form = NewPostForm(data={'picture': 'github1.jpg', 'caption': 'Some caption', 'tags': 'Some tags'},)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        form = NewPostForm(data={'picture': "", 'caption': "", 'tags': ""})
        self.assertFalse(form.is_valid())
                           