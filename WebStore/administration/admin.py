from django.contrib import admin
from .models import Settings

# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'is_visitable', 'is_sellable', 'contact_email', 'contact_manager')

admin.site.register(Settings, SettingsAdmin)