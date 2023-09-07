from django.db import models


class Season(models.Model):
    """Season model class"""

    season_number = models.IntegerField()
    franchise = models.ForeignKey(
        "Franchise", on_delete=models.CASCADE, related_name="seasons")
    premier_date = models.CharField(max_length=10)
