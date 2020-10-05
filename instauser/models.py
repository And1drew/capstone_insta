from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InstaUser(AbstractUser):
    follwing = models.ManyToManyField('self', related_name='user_following', symmetrical=False)