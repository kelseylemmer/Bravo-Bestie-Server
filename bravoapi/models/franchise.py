from django.db import models


class Franchise(models.Model):
    """Franchise Model class"""

    label = models.CharField(max_length=70)
    abbreviation = models.CharField(max_length=10)
    series_premier = models.CharField(max_length=10)
