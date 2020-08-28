from django.contrib import admin
from .models import CartItem, Order, OrderItem, Promo

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'amount')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'order', 'unit_price', 'amount', 'product')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_gender', 'user_contact_phone_no', 'shipping_fee', 'total_amount', 'status', 'payment', 'remittance_account', 'timestamp', 'is_canceled')
    inlines = [OrderItemInline]

class PromoAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_amount', 'discount_ratio', 'discount_limit', 'has_total_amount_limit', 'total_amount_limit', 'has_total_count_limit', 'total_count_limit', 'has_time_limit', 'time_limit_start', 'time_limit_expire')

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Promo, PromoAdmin)