from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile Model class"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=1000)
    picture = models.URLField(max_length=100)
    episodes = models.ManyToManyField("Episode", through="ProfileEpisode")
    favorite_franchise = models.ForeignKey(
        'Franchise', on_delete=models.CASCADE)
    # stretch goal: add top 5 cast members
