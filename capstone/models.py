from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Issue(models.Model):
    issue = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
