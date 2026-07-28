"""
Students Forms
"""
from django import forms
from .models import Student
import re


class StudentRegistrationForm(forms.ModelForm):
    MATRIC_PATTERNS = [
        r'^U21/CPS/\d{4}$',
        r'^U22/CPS/\d{4}$',
        r'^U23/CPS/\d{4}$',
    ]

    class Meta:
        model = Student
        exclude = ['user', 'is_approved', 'is_class_rep', 'created_at', 'updated_at']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'contact_address': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Contact Address', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'matric_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'U23/CPS/0001'}),
            'relationship_status': forms.Select(attrs={'class': 'form-select'}),
            'favourite_course_mate': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Favourite Course Mate\'s Name'}),
            'alternative_course': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Mathematics, Physics'}),
            'favourite_programming_language': forms.Select(attrs={'class': 'form-select'}),
            'bio': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Tell us about yourself...', 'rows': 4}),
            'quote': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your favourite quote...', 'rows': 2}),
            'skills': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'e.g., Python, Web Development, Data Analysis', 'rows': 2}),
            'image': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
        }

    def clean_matric_number(self):
        matric = self.cleaned_data.get('matric_number', '').upper().strip()
        valid = any(re.match(pattern, matric, re.IGNORECASE) for pattern in self.MATRIC_PATTERNS)
        if not valid:
            raise forms.ValidationError(
                "Invalid matric number. Format must be U21/CPS/XXXX, U22/CPS/XXXX, or U23/CPS/XXXX"
            )
        if Student.objects.filter(matric_number__iexact=matric).exists():
            raise forms.ValidationError("This matric number is already registered.")
        return matric

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()
        if Student.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'matric_number', 'is_approved', 'is_class_rep', 'created_at', 'updated_at']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'contact_address': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'relationship_status': forms.Select(attrs={'class': 'form-select'}),
            'favourite_course_mate': forms.TextInput(attrs={'class': 'form-input'}),
            'alternative_course': forms.TextInput(attrs={'class': 'form-input'}),
            'favourite_programming_language': forms.Select(attrs={'class': 'form-select'}),
            'bio': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'quote': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2}),
            'skills': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 2}),
            'image': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
        }
