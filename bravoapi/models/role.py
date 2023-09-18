from django.db import models


class Role(models.Model):
    """Role Model class"""

    label = models.CharField(max_length=30)
