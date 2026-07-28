"""
Admin Portal Forms
"""
from django import forms
from lecturers.models import Lecturer
from school_pages.models import SchoolPage
from core.models import FormControl, SiteSettings
from students.models import Student


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Dr., Prof., Mr., Mrs.'}),
            'lecturer_type': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'department': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'specialization': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'order': forms.NumberInput(attrs={'class': 'form-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


class SchoolPageForm(forms.ModelForm):
    class Meta:
        model = SchoolPage
        fields = '__all__'
        widgets = {
            'page_type': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 6}),
            'office': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


class FormControlForm(forms.ModelForm):
    class Meta:
        model = FormControl
        fields = '__all__'
        widgets = {
            'is_enabled': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'opening_date': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'closing_date': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Custom message to display on the site'}),
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-input'}),
            'site_tagline': forms.TextInput(attrs={'class': 'form-input'}),
            'department': forms.TextInput(attrs={'class': 'form-input'}),
            'university': forms.TextInput(attrs={'class': 'form-input'}),
            'cover_photo': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'primary_color': forms.TextInput(attrs={'class': 'form-input', 'type': 'color'}),
            'accent_color': forms.TextInput(attrs={'class': 'form-input', 'type': 'color'}),
            'show_yearbook_link': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'yearbook_message': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2}),
        }


class StudentStatusForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['is_approved', 'is_class_rep']
        widgets = {
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'is_class_rep': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
