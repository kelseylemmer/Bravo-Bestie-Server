from django.db import models


class Review(models.Model):
    """ProfileReview model class"""

    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE)
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date = models.DateTimeField()
