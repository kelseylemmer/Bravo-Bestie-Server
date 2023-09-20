from django.db import models


class FranchiseCast(models.Model):
    """Franchise Cast model class"""

    cast = models.ForeignKey(
        'Cast', on_delete=models.CASCADE)
    franchise = models.ForeignKey(
        'Franchise', on_delete=models.CASCADE)
