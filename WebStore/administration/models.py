from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Configuration(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='網站名稱')
    site_logo_small = models.ImageField(upload_to='administration', verbose_name='網站Logo（小）')
    site_logo_large = models.ImageField(upload_to='administration', verbose_name='網站Logo（大）')
    is_visitable = models.BooleanField(default=True, verbose_name='允許造訪網站')
    is_sellable = models.BooleanField(default=True, verbose_name='允許顧客成立訂單')
    manager_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='管理員')
    manager_name = models.CharField(max_length=100, verbose_name='管理員姓名')
    manager_contact_phone_no = models.CharField(max_length=20, verbose_name='管理員聯絡電話')
    manager_email = models.CharField(max_length=100, verbose_name='管理員電子郵件信箱')
    manager_address = models.CharField(max_length=200, verbose_name='管理員地址')
    manager_bank_name = models.CharField(max_length=20, verbose_name='收款銀行名稱')
    manager_bank_code = models.CharField(max_length=5, verbose_name='收款銀行代碼')
    manager_receiving_account = models.CharField(max_length=30, verbose_name='收款帳號')
    shipping_fee = models.IntegerField(default=60, verbose_name='每筆訂單運費')
    copyright_info = models.CharField(max_length=200, verbose_name='權利聲明')

class UserProfile(models.Model):
    GENDER_CHOICES = ((0, '先生'), (1, '女士'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    shipping_postal_code = models.CharField(max_length=5, blank=True)
    shipping_address = models.CharField(max_length=200, blank=True)
    contact_phone_no = models.CharField(max_length=20, blank=True)