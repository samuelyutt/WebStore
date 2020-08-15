from django.contrib import admin
from .models import CartItem, Order, OrderItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'amount')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'order', 'unit_price', 'amount', 'product')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_gender', 'shipping_fee', 'total_amount', 'status', 'payment', 'timestamp', 'is_canceled')
    inlines = [OrderItemInline]


admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)