from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Settings, UserProfile

# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'is_visitable', 'is_sellable', 'contact_email', 'contact_manager')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'shipping_address')

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.register(Settings, SettingsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)