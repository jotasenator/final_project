from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Issue(models.Model):
    issue = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10, default="")
    picture = models.ImageField(
        upload_to="profile_pictures/"
    )  # /media/profile_pictures/user1.jpg
