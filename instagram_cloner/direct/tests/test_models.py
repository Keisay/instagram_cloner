{# Old test to update #}

import uuid
import datetime

from django.test import TestCase
from django.core.files import File
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from direct.models import Message
from django.urls import reverse


class TestMessageModel(TestCase):
    def test_message_model(self):
        user1 = User.objects.create(username='Real')
        sender1 = User.objects.create(username='Loki')
        recipient1 = User.objects.create(username='Greed')
        
        Message.objects.create(
            user=user1,
            sender=sender1,
            recipient=recipient1,
            body='Some text',
            date=datetime.datetime.now(),
            is_read=False,
        )