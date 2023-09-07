from django.db import models


class Episode(models.Model):
    """Episode model class"""

    title = models.CharField(max_length=60)
    synopsis = models.CharField(max_length=1000)
    runtime = models.IntegerField()
    season = models.ForeignKey(
        "Season", on_delete=models.CASCADE, related_name="episodes")
    episode = models.IntegerField()
    air_date = models.DateTimeField()
