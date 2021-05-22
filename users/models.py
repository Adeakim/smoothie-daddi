from typing import BinaryIO
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='profile.jgp',upload_to='Profile_pics')
    bio=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=11)
