{# Old test to update #}

import uuid
import datetime

from django.test import TestCase
from django.core.files import File
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from comment.models import Comment
from post.models import Post
from django.urls import reverse


class TestCommentModel(TestCase):
    def test_comment_model(self):
        post1 = Post.objects.create(
            id = uuid.uuid4(),
            caption = 'Dummy caption',
        )
        
        user1 = User.objects.create(username='GodDog')
        
        Comment.objects.create(
            post=post1,
            user=user1,
            body='Some text',
            date=datetime.datetime.now(),
        )