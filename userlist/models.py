from datetime import datetime
import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Userlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    secret = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=False)
    create_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)

    USERNAME_FILE = 'user_name'

    def get_id(self):
        return self.id