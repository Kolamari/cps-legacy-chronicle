"""
Lecturers Model - CPS Legacy Chronicle
"""
from django.db import models


class Lecturer(models.Model):
    LECTURER_TYPE = [
        ('senior', 'Senior Lecturer'),
        ('junior', 'Junior Lecturer'),
    ]

    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100, help_text="e.g., Dr., Prof., Mr., Mrs.")
    lecturer_type = models.CharField(max_length=10, choices=LECTURER_TYPE, default='senior')
    photo = models.ImageField(upload_to='lecturers/', blank=True, null=True)
    email = models.EmailField(blank=True)
    department = models.CharField(max_length=200, default="Computer Science")
    message = models.TextField(blank=True, help_text="Message or description")
    specialization = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.title} {self.full_name}"
