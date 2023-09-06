from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=1000)
    picture = models.CharField(max_length=100)
    episodes = models.ManyToManyField("Episode", through="UserEpisode")
