{# Old test to update #}

import uuid
import datetime

from django.test import TestCase
from django.core.files import File
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from notifications.models import Notification
from post.models import Post
from django.urls import reverse

class TestNotificationModel(TestCase):
    def test_notification_model(self):
        post1 = Post.objects.create(id=uuid.uuid4())
        sender1 = User.objects.create(username='Grak')
        user1 = User.objects.create(username='Billy')
        
        Notification.objects.create(
            post=post1,
            sender=sender1,
            user=user1,
            notification_type=1,
            text_preview='Some preview',
            date=datetime.datetime.now(),
            is_seen=False,
        )