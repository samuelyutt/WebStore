from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField(max_length=200)
    site_logo_small = models.ImageField(upload_to='administration')
    site_logo_large = models.ImageField(upload_to='administration')
    is_visitable = models.BooleanField(default=True)
    is_sellable = models.BooleanField(default=True)
    contact_manager = models.CharField(max_length=100)
    contact_phone_no = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=200)
    copyright_info = models.CharField(max_length=200)