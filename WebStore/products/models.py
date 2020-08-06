from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    utility = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name