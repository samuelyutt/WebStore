from django.contrib import admin
from .models import Category, Product, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'unit_price', 'inventory_quantity', 'utility', 'ingredient', 'description')
    inlines = [ImageInline]

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)