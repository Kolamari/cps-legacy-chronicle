"""
Core Context Processors
"""
from .models import FormControl, SiteSettings


def form_status(request):
    try:
        control = FormControl.get_instance()
        return {
            'form_control': control,
            'form_status': control.get_status(),
            'form_status_display': control.get_status_display_name(),
            'is_registration_open': control.is_registration_open(),
        }
    except:
        return {
            'form_control': None,
            'form_status': 'closed',
            'form_status_display': 'Registration Closed',
            'is_registration_open': False,
        }


def site_settings(request):
    try:
        settings = SiteSettings.get_instance()
        return {
            'site_settings': settings,
        }
    except:
        return {
            'site_settings': None,
        }
