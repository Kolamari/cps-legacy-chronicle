"""
Core Models - Form Control and Site Settings
"""
from django.db import models
from django.utils import timezone


class FormControl(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closing_soon', 'Closing Soon'),
        ('closed', 'Closed'),
    ]

    is_enabled = models.BooleanField(default=True, help_text="Enable or disable registration manually")
    opening_date = models.DateTimeField(null=True, blank=True, help_text="When registration opens")
    closing_date = models.DateTimeField(null=True, blank=True, help_text="When registration closes")
    message = models.TextField(blank=True, help_text="Custom message to display")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Form Control"
        verbose_name_plural = "Form Controls"

    def __str__(self):
        return f"Registration: {self.get_status()}"

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def get_status(self):
        if not self.is_enabled:
            return 'closed'
        now = timezone.now()
        if self.opening_date and now < self.opening_date:
            return 'closed'
        if self.closing_date:
            time_until_close = self.closing_date - now
            if time_until_close.total_seconds() <= 0:
                return 'closed'
            if time_until_close.days <= 3:
                return 'closing_soon'
        return 'open'

    def get_status_display_name(self):
        status = self.get_status()
        mapping = {
            'open': 'Registration Open',
            'closing_soon': 'Registration Closing Soon',
            'closed': 'Registration Closed',
        }
        return mapping.get(status, 'Unknown')

    def is_registration_open(self):
        return self.get_status() in ['open', 'closing_soon']


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="CPS Legacy Chronicle")
    site_tagline = models.CharField(max_length=300, default="Class of 2026 - Computer Science Department")
    department = models.CharField(max_length=200, default="Computer Science")
    university = models.CharField(max_length=300, default="University Name")
    cover_photo = models.ImageField(upload_to='school/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0A1F44")
    accent_color = models.CharField(max_length=7, default="#D4AF37")
    show_yearbook_link = models.BooleanField(default=False)
    yearbook_message = models.TextField(blank=True, default="The yearbook will be available soon.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
