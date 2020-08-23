from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=200, verbose_name='類別名稱')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='類別')
    name = models.CharField(max_length=200, verbose_name='名稱')
    utility = models.CharField(max_length=200, verbose_name='用途')
    ingredient = models.CharField(max_length=200, verbose_name='成分')
    description = models.TextField(blank=True, verbose_name='概覽')
    unit_price = models.IntegerField(default=0, verbose_name='單價')
    is_sellable = models.BooleanField(default=True, verbose_name='上架')
    inventory_quantity = models.IntegerField(default=0, verbose_name='庫存')
    cover_image = models.ImageField(blank=True, verbose_name='封面照片')

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='產品')
    image = models.ImageField(verbose_name='照片')