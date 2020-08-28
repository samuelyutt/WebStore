from datetime import datetime
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

    def is_valid(self):
        return self.amount <= self.product.inventory_quantity and self.product.is_sellable

    def total_amounts(self):
        return self.product.unit_price * self.amount


class Order(models.Model):
    GENDER_CHOICES = ((0, '先生'), (1, '女士'))
    STATUS_CHOICES = ((0, '已初始'), (1, '已成立'), (2, '已確認收到付款'), (3, '已出貨'), (4, '已完成'),
                      (5, '已申請退回'), (6, '已收到退回商品'), (7, '已退款'))
    PAYMENT_CHOICES = ((0, 'ATM匯款'),)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name='使用者')
    user_name = models.CharField(max_length=100, verbose_name='收件人')
    user_gender = models.IntegerField(default=0, choices=GENDER_CHOICES, verbose_name='稱謂')
    user_contact_phone_no = models.CharField(max_length=20, verbose_name='聯絡電話')
    shipping_postal_code = models.CharField(max_length=5, verbose_name='郵遞區號')
    shipping_address = models.CharField(max_length=200, verbose_name='收件地址')
    shipping_fee = models.IntegerField(default=60, verbose_name='運費')
    total_amount = models.IntegerField(verbose_name='總金額')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, verbose_name='狀態')
    payment = models.IntegerField(default=0, choices=PAYMENT_CHOICES, verbose_name='付款方式')
    remittance_account = models.CharField(blank=True, max_length=5, verbose_name='匯款帳號末五碼')
    is_canceled = models.BooleanField(default=False, verbose_name='已取消')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='成立時間')


    def __str__(self):
        return '訂單 ' + str(self.id)

    def cal_total_amounts(self):
        total_amounts = self.shipping_fee
        for item in self.orderitem_set.all():
            total_amounts += item.total_amounts()
        return total_amounts if total_amounts > 0 else 0

    def admin_status_description(self):
        if self.status == 0:
            return '等待顧客確認運送資料'
        elif self.status == 1 and self.payment == 0:
            if self.remittance_account:
                return '顧客已填寫匯款帳號：' + str(self.remittance_account)
            else:
                return '等待顧客填寫匯款帳號'
        elif self.status == 2:
            return '已確認收到付款'
        elif self.status == 3:
            return '已出貨'
        else:
            return self.get_status_display()

    def customer_status_description(self):
        if self.status == 0:
            return '感謝您！您的訂單已成立！\n請填寫運送資料並送出。'
        elif self.status == 1 and self.payment == 0:
            if self.remittance_account:
                return '請稍候！我們會盡快核對款項並出貨！'
            else:
                return '運送資料已送出！\n當您匯款完成後，請填寫匯款帳戶末五碼。'
        elif self.status == 2:
            return '我們已確認您的付款，將盡快安排出貨！'
        elif self.status == 3:
            return '好消息！您的訂單已出貨！'
        elif self.status == 4:
            return '您的訂單已完成！'
        else:
            return self.get_status_display()

    def customer_short_status_description(self):
        if self.status == 0:
            return '請填寫運送資料'
        elif self.status == 1 and self.payment == 0:
            if self.remittance_account:
                return '正在核對款項'
            else:
                return '請填寫匯款帳戶'
        elif self.status == 2:
            return '已確認您的付款'
        elif self.status == 3:
            return '已出貨'
        elif self.status == 4:
            return '已完成'
        else:
            return self.get_status_display()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    unit_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.item_name) + '(' + str(self.amount) + ')'

    def total_amounts(self):
        return self.unit_price * self.amount


class Promo(models.Model):
    DISCOUNT_TYPE_CHOICES = ((0, '總金額折價'), (1, '總金額打折'), (2, '免運費'))
    HAS_LIMIT_CHOICES = ((0, '無'), (1, '有'))

    code = models.CharField(max_length=32, unique=True, verbose_name='優惠代碼')
    
    # Discount Type
    discount_type = models.IntegerField(default=0, choices=DISCOUNT_TYPE_CHOICES, verbose_name='優惠類型')
    discount_amount = models.IntegerField(default=0, verbose_name='折價金額')
    discount_ratio = models.DecimalField(default=0.9, max_digits=3, decimal_places=2, verbose_name='打折（比例）')
    discount_limit = models.IntegerField(default=100, verbose_name='最高折價上限')
    
    # Limitations
    has_total_amount_limit = models.IntegerField(default=0, choices=HAS_LIMIT_CHOICES, verbose_name='消費滿額才可用限制')
    total_amount_limit = models.IntegerField(default=0, verbose_name='消費滿此金額可用')
    
    has_total_count_limit = models.IntegerField(default=0, choices=HAS_LIMIT_CHOICES, verbose_name='數量限制')
    total_count_limit = models.IntegerField(default=10, verbose_name='剩餘數量')
    
    has_time_limit = models.IntegerField(default=0, choices=HAS_LIMIT_CHOICES, verbose_name='使用時間限制')
    time_limit_start = models.DateTimeField(default=datetime.now, verbose_name='開始有效時間')
    time_limit_expire = models.DateTimeField(default=datetime.now, verbose_name='截止有效時間')
    
    def __str__(self):
        return str(self.code)

    def usage_description(self):
        return self.total_amount_limit_description() + \
               self.discount_type_description() + \
               self.time_limit_description() + \
               self.total_count_limit_description()

    def discount_type_description(self):
        ratio_digits1 = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        ratio_digits2 = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        ret = ''
        if self.discount_type == 0:
            ret += '消費金額折' + str(self.discount_amount)
        elif self.discount_type == 1:
            discount_str = str(self.discount_ratio)
            ratio_str = ratio_digits1[int(discount_str[2])] + ratio_digits2[int(discount_str[3])] + '折'
            ret += '消費金額' + ratio_str
            ret += '，折抵金額上限NT$ ' + str(self.discount_limit)
            print(str(self.discount_ratio)[2])
        elif self.discount_type == 2:
            ret += '免運費'
        return ret + '。'

    def total_amount_limit_description(self):
        ret = ''
        if self.has_total_amount_limit == 1:
            ret += '消費金額滿NT$ ' + str(self.total_amount_limit)
        else:
            ret += '不限消費金額'
        return ret + '可使用。'

    def time_limit_description(self):
        ret = '使用期限'
        if self.has_time_limit == 1:
            ret += '自' + str(self.time_limit_start) + '至' + str(self.time_limit_expire) + '止'
        else:
            ret += '無限制'
        return ret + '。'

    def total_count_limit_description(self):
        ret = '剩餘數量：'
        if self.has_total_count_limit == 1:
            ret += str(self.total_count_limit) + '張'
        else:
            ret += '無限制'
        return ret + '。'