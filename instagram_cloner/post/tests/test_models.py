{# Old test to update #}

import uuid
import datetime

from django.test import TestCase
from django.core.files import File
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from post.models import Tag, Post, Follow, Stream, Likes
from django.urls import reverse

# Create your tests here.

# TEST of TAG Model
class TestTagModels(TestCase):
    def test_tag_model(self):
        tag = Tag.objects.create(
            title = 'Tag Title',
            slug = 'Slug text',
        )

class TestTagStrModel(TestCase):
    def test_tag_str(self):
        tag_lebron = Tag.objects.create(title='lebron_tag')
        self.assertEqual(str(tag_lebron), 'lebron_tag')
# END-TEST of TAG MODEL


       
# TEST of POST Model
class TestPostModels(TestCase):
    def test_post_model(self):
        post = Post.objects.create(
            id = uuid.uuid4(),
            picture = ImageFile('C:/Users/alexi/Desktop/socialgram/socialgram/media/github1.jpg'),
            caption = 'Dummy caption',
            posted = datetime.datetime.now(),
            likes = 2,
        )   

class TestCountTagModel(TestCase):
    def test_tag_has_a_post(self):
        post = Post.objects.create(caption='Striving for Greatness')
        tag1 = Tag.objects.create(title='Aaron')
        tag2 = Tag.objects.create(title='Baron')
        tag1.post_set.add(post)
        tag2.post_set.add(post)
        self.assertEqual(post.tags.count(), 2)
        
class TestPostUserModel(TestCase):
    def test_post_user_foreignkey(self):
        user1 = User.objects.create(first_name='Kevino')
        Post.objects.create(
            id = uuid.uuid4(),
            caption = 'Dummy caption',
            posted = datetime.datetime.now(),
            user=user1
        )
# END-TEST of POST Model



# TEST of FOLLOW Model
class TestFollowModel(TestCase):
    def test_follow_has_follower_following(self):
        user = User.objects.create_user(username='user1')
        user2 = User.objects.create_user(username='user2')
        
        Follow.objects.create(
            follower=user,
            following=user2,
        )
# END-TEST of FOLLOW Model



# TEST of STREAM Model
class TestStreamModel(TestCase):
    def test_stream_model(self):
        user = User.objects.create_user(username='user1')
        post = Post.objects.create(
            id=uuid.uuid4(),
            caption = 'Dummy caption',
            posted = datetime.datetime.now(),
            likes = 2,
        )
        
        Stream.objects.create(
            following=user,
            user=user,
            post=post,
            date = datetime.datetime.now(),
        )
# END-TEST of STREAM Model



# TEST of LIKES Model
class TestLikesModel(TestCase):
    def test_likes_from_user(self):
        user = User.objects.create_user(username='Bonbon')
        post = Post.objects.create(
            id=uuid.uuid4(),
            caption = 'Dummy caption',
            posted = datetime.datetime.now(),
            likes = 2,
        )
        
        Likes.objects.create(
            user=user,
            post=post,
        )
# END-TEST of LIKES Model