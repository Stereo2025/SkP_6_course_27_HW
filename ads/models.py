from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
