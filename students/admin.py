"""
Students Admin
"""
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'matric_number', 'email', 'favourite_programming_language', 'is_approved', 'is_class_rep', 'created_at']
    list_filter = ['is_approved', 'is_class_rep', 'favourite_programming_language', 'relationship_status']
    search_fields = ['full_name', 'matric_number', 'email', 'bio', 'skills']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Info', {'fields': ('user', 'full_name', 'email', 'phone_number', 'image')}),
        ('Academic Info', {'fields': ('matric_number', 'favourite_programming_language', 'alternative_course')}),
        ('Social', {'fields': ('relationship_status', 'favourite_course_mate')}),
        ('Profile', {'fields': ('bio', 'quote', 'skills', 'contact_address')}),
        ('Status', {'fields': ('is_approved', 'is_class_rep')}),
        ('Class Rep', {'fields': ('message_to_class', 'responsibilities')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
