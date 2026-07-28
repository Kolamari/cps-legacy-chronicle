"""
Lecturers Admin
"""
from django.contrib import admin
from .models import Lecturer


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'lecturer_type', 'department', 'is_active', 'order']
    list_filter = ['lecturer_type', 'is_active', 'department']
    search_fields = ['full_name', 'title', 'specialization']
    ordering = ['order', 'full_name']
