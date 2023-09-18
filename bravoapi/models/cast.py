from django.db import models


class Cast(models.Model):
    """Cast model class"""

    name = models.CharField(max_length=40)
    img_url = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
