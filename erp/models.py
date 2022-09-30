from django.db import models

# Create your models here.

class Inventory(models.Model):

    Type = models.CharField(max_length=100)
    Brand = models.CharField(max_length=50)
    Size = models.IntegerField()
    Colour = models.CharField(max_length=50)
    Price = models.IntegerField()
    Quantity = models.CharField(max_length=50)