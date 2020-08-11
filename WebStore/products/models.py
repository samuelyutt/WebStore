from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    utility = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    unit_price = models.IntegerField(default=0)
    is_unit_sellable = models.BooleanField(default=True)
    inventory_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()