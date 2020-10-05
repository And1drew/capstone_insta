from django.db import models
from django.utils import timezone
from instauser.models import InstaUser

# Create your models here.
class Post(models.Model):
    post = models.TextField(max_length=280)
    time_date = models.DateTimeField(default=timezone.now)
    insta_user = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name="insta_user")