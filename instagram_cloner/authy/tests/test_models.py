{# Old test to update #}

import uuid
import datetime

from django.test import TestCase
from django.core.files import File
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from authy.models import Profile
from post.models import Post
from django.urls import reverse


class TestProfileModel(TestCase):
    def test_profile(self):
        user = User.objects.create_user(username='user3')
        
                
        Profile.objects.create(
            user=user,
            first_name='Kendrick',
            last_name='Lamar',
            location='Paris',
            url='neverstopgrinding.com',
            profile_info='The best of me',
            created=datetime.datetime.now(),
        )