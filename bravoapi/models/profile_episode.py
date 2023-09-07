from django.db import models


class ProfileEpisode(models.Model):
    """ProfileEpisode model class"""

    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE)
    episode = models.ForeignKey(
        'Episode', on_delete=models.CASCADE)
