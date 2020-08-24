from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Configuration, UserProfile

# Register your models here.
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'is_visitable', 'is_sellable', 'manager_email', 'manager_name')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'contact_phone_no', 'shipping_postal_code', 'shipping_address')

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)