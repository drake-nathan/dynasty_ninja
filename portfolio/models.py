from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    sleeper_username = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=CASCADE)
    date_updated = models.DateTimeField(auto_now=True)