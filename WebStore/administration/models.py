from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Settings(models.Model):
    class Meta:
        verbose_name_plural = "settings"
    
    site_name = models.CharField(max_length=200)
    site_logo_small = models.ImageField(upload_to='administration')
    site_logo_large = models.ImageField(upload_to='administration')
    is_visitable = models.BooleanField(default=True)
    is_sellable = models.BooleanField(default=True)
    manager_user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=100)
    manager_contact_phone_no = models.CharField(max_length=20)
    manager_email = models.CharField(max_length=100)
    manager_address = models.CharField(max_length=200)
    manager_bank_name = models.CharField(max_length=20)
    manager_bank_code = models.CharField(max_length=5)
    manager_bank_code = models.CharField(max_length=5)
    manager_receiving_account = models.CharField(max_length=30)
    copyright_info = models.CharField(max_length=200)

class UserProfile(models.Model):
    GENDER_CHOICES = ((0, '先生'), (1, '女士'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    shipping_postal_code = models.CharField(max_length=5, blank=True)
    shipping_address = models.CharField(max_length=200, blank=True)
    contact_phone_no = models.CharField(max_length=20, blank=True)