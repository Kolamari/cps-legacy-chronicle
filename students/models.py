"""
Students Model - CPS Legacy Chronicle
"""
from django.db import models
from django.conf import settings
import re


class Student(models.Model):
    RELATIONSHIP_STATUS = [
        ('single', 'Single'),
        ('in_relationship', 'In a Relationship'),
        ('married', 'Married'),
        ('prefer_not', 'Prefer Not to Say'),
    ]

    PROGRAMMING_LANGUAGES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('c_cpp', 'C/C++'),
        ('csharp', 'C#'),
        ('php', 'PHP'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('swift', 'Swift'),
        ('kotlin', 'Kotlin'),
        ('ruby', 'Ruby'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_address = models.TextField()
    phone_number = models.CharField(max_length=20)
    matric_number = models.CharField(max_length=20, unique=True)
    relationship_status = models.CharField(max_length=20, choices=RELATIONSHIP_STATUS)
    favourite_course_mate = models.CharField(max_length=200, blank=True)
    alternative_course = models.CharField(max_length=200, help_text="If not Computer Science, what else?")
    favourite_programming_language = models.CharField(max_length=20, choices=PROGRAMMING_LANGUAGES)
    bio = models.TextField(blank=True, help_text="Short bio about yourself")
    quote = models.TextField(blank=True, help_text="Your favourite quote")
    skills = models.TextField(blank=True, help_text="List your skills separated by commas")
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_class_rep = models.BooleanField(default=False)
    responsibilities = models.TextField(blank=True, help_text="Class rep responsibilities")
    message_to_class = models.TextField(blank=True, help_text="Message to the class")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} ({self.matric_number})"

    @classmethod
    def validate_matric(cls, matric):
        patterns = [
            r'^U21/CPS/\d{4}$',
            r'^U22/CPS/\d{4}$',
            r'^U23/CPS/\d{4}$',
        ]
        for pattern in patterns:
            if re.match(pattern, matric, re.IGNORECASE):
                return True
        return False

    def get_initials(self):
        names = self.full_name.split()
        if len(names) >= 2:
            return f"{names[0][0]}{names[-1][0]}".upper()
        return self.full_name[:2].upper()
