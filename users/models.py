from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    phone = models.CharField(max_length=13)
