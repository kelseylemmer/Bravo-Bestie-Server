from django.db import models


class SeasonCast(models.Model):
    """Franchise Cast model class"""

    cast = models.ForeignKey(
        'Cast', on_delete=models.CASCADE)
    season = models.ForeignKey(
        'Season', on_delete=models.CASCADE)
    role = models.ForeignKey(
        'Role', on_delete=models.CASCADE)
