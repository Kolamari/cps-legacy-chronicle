"""
School Pages Admin
"""
from django.contrib import admin
from .models import SchoolPage


@admin.register(SchoolPage)
class SchoolPageAdmin(admin.ModelAdmin):
    list_display = ['page_type', 'full_name', 'title', 'is_active', 'order']
    list_filter = ['page_type', 'is_active']
    search_fields = ['full_name', 'title']
    ordering = ['order']
