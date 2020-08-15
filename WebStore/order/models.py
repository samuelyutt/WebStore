from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product) + '(' + str(self.amount) + ')'


class Order(models.Model):
    GENDER_CHOICES = ((0, '先生'), (1, '女士'))
    STATUS_CHOICES = ((0, '已初始'), (1, '已成立'), (2, '已確認收到付款'), (3, '已出貨'), (4, '已完成'),
                      (5, '已申請退回'), (6, '已收到退回商品'), (7, '已退款'))
    PAYMENT_CHOICES = ((0, 'ATM匯款'),)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=100)
    user_gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    shipping_postal_code = models.CharField(max_length=6)
    shipping_address = models.CharField(max_length=200)
    shipping_fee = models.IntegerField(default=60)
    total_amount = models.IntegerField()
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    payment = models.IntegerField(default=0, choices=PAYMENT_CHOICES)
    remittance_account = models.CharField(blank=True, max_length=5)
    is_canceled = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    unit_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.item_name) + '(' + str(self.amount) + ')'