from django.db import models


class Book(models.Model):
    """Book model class"""

    title = models.CharField(max_length=40)
    pages = models.IntegerField()
    synopsis = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=50)
    img_url = models.URLField()
    publish_date = models.CharField(max_length=10)
    cast = models.ForeignKey('Cast', on_delete=models.CASCADE)
    purchase = models.CharField(max_length=200)
