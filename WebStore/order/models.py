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
    STATUS_CHOICES = ((u'0', '已初始'), (u'1', '已成立'), (u'2', '已付款'), (u'3', '已出貨'), (u'4', '已完成'),
                      (u'5', '已申請退回'), (u'6', '已收到退回商品'), (u'7', '已退款'))
    PAYMENT_CHOICES = ((u'0', 'ATM匯款'),)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    shipping_fee = models.IntegerField(default=60)
    total_amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    is_canceled = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    unit_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.item_name) + '(' + str(self.amount) + ')'