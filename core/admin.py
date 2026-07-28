"""
Core Admin Configuration
"""
from django.contrib import admin
from .models import FormControl, SiteSettings


@admin.register(FormControl)
class FormControlAdmin(admin.ModelAdmin):
    list_display = ['is_enabled', 'opening_date', 'closing_date', 'get_status', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_status(self, obj):
        return obj.get_status_display_name()
    get_status.short_description = 'Current Status'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'department', 'university', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
