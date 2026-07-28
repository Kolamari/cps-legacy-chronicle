# """
# School Pages Model - CPS Legacy Chronicle
# """
# from django.db import models


# class SchoolPage(models.Model):
#     PAGE_TYPES = [
#         ('vc', 'Vice Chancellor'),
#         ('faculty', 'Faculty of Science'),
#         ('hod', 'Head of Department'),
#         ('ict', 'Director of ICT'),
#     ]

#     page_type = models.CharField(max_length=20, choices=PAGE_TYPES, unique=True)
#     full_name = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     photo = models.ImageField(upload_to='school/', blank=True, null=True)
#     message = models.TextField(help_text="Welcome message")
#     description = models.TextField(help_text="Official description")
#     office = models.CharField(max_length=300, blank=True)
#     email = models.EmailField(blank=True)
#     order = models.PositiveIntegerField(default=0)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['order']

#     def __str__(self):
#         return f"{self.get_page_type_display()} - {self.full_name}"

#     @classmethod
#     def get_or_create_defaults(cls):
#         defaults = [
#             {
#                 'page_type': 'vc',
#                 'full_name': 'Professor John Doe',
#                 'title': 'Vice Chancellor',
#                 'message': 'Welcome to the Computer Science Department. We are committed to excellence in education and research.',
#                 'description': 'The Vice Chancellor is the chief executive officer of the university, responsible for the overall administration and academic leadership.',
#                 'office': 'Vice Chancellor\'s Office, Main Campus',
#                 'order': 1,
#             },
#             {
#                 'page_type': 'faculty',
#                 'full_name': 'Dr. Jane Smith',
#                 'title': 'Dean, Faculty of Science',
#                 'message': 'The Faculty of Science is dedicated to producing world-class graduates in various scientific disciplines.',
#                 'description': 'The Faculty of Science encompasses several departments including Computer Science, Mathematics, Physics, Chemistry, and Biology.',
#                 'office': 'Dean\'s Office, Faculty of Science',
#                 'order': 2,
#             },
#             {
#                 'page_type': 'hod',
#                 'full_name': 'Dr. Michael Johnson',
#                 'title': 'Head of Department, Computer Science',
#                 'message': 'Welcome to the Computer Science Department. Our mission is to nurture the next generation of tech leaders.',
#                 'description': 'The Head of Department oversees all academic and administrative activities within the Computer Science Department.',
#                 'office': 'HOD Office, Computer Science Department',
#                 'order': 3,
#             },
#             {
#                 'page_type': 'ict',
#                 'full_name': 'Engr. Sarah Williams',
#                 'title': 'Director of ICT',
#                 'message': 'The ICT Directorate is committed to providing cutting-edge technology infrastructure for the university community.',
#                 'description': 'The Director of ICT oversees all information and communication technology services across the university.',
#                 'office': 'ICT Directorate, Main Campus',
#                 'order': 4,
#             },
#         ]
#         for data in defaults:
#             cls.objects.get_or_create(page_type=data['page_type'], defaults=data)
"""
School Pages Model - CPS Legacy Chronicle
"""
from django.db import models


class SchoolPage(models.Model):
    PAGE_TYPES = [
        ('vc', 'Vice Chancellor'),
        ('faculty', 'Faculty of Science'),
        ('hod', 'Head of Department'),
        ('ict', 'Director of ICT'),
        ('ippto', 'IPPTO Director'),
    ]

    page_type = models.CharField(max_length=20, choices=PAGE_TYPES, unique=True)
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='school/', blank=True, null=True)
    message = models.TextField(help_text="Welcome message")
    description = models.TextField(help_text="Official description")
    office = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_page_type_display()} - {self.full_name}"

    @classmethod
    def get_or_create_defaults(cls):
        defaults = [
            {
                'page_type': 'vc',
                'full_name': 'Professor John Doe',
                'title': 'Vice Chancellor',
                'message': 'Welcome to the Computer Science Department. We are committed to excellence in education and research.',
                'description': 'The Vice Chancellor is the chief executive officer of the university, responsible for the overall administration and academic leadership.',
                'office': 'Vice Chancellor\'s Office, Main Campus',
                'order': 1,
            },
            {
                'page_type': 'faculty',
                'full_name': 'Dr. Jane Smith',
                'title': 'Dean, Faculty of Science',
                'message': 'The Faculty of Science is dedicated to producing world-class graduates in various scientific disciplines.',
                'description': 'The Faculty of Science encompasses several departments including Computer Science, Mathematics, Physics, Chemistry, and Biology.',
                'office': 'Dean\'s Office, Faculty of Science',
                'order': 2,
            },
            {
                'page_type': 'hod',
                'full_name': 'Dr. Michael Johnson',
                'title': 'Head of Department, Computer Science',
                'message': 'Welcome to the Computer Science Department. Our mission is to nurture the next generation of tech leaders.',
                'description': 'The Head of Department oversees all academic and administrative activities within the Computer Science Department.',
                'office': 'HOD Office, Computer Science Department',
                'order': 3,
            },
            {
                'page_type': 'ict',
                'full_name': 'Engr. Sarah Williams',
                'title': 'Director of ICT',
                'message': 'The ICT Directorate is committed to providing cutting-edge technology infrastructure for the university community.',
                'description': 'The Director of ICT oversees all information and communication technology services across the university.',
                'office': 'ICT Directorate, Main Campus',
                'order': 4,
            },
            {
                'page_type': 'ippto',
                'full_name': 'Dr. Aliyu Ibrahim',
                'title': 'IPPTO Director',
                'message': 'Welcome to the Intellectual Property and Technology Transfer Office. We protect and nurture academic innovations.',
                'description': 'The IPPTO Director coordinates patent registration, copyright protection, and technology commercialization policies for university-born discoveries.',
                'office': 'IPPTO Directorate, Central Administration Block',
                'order': 5,
            },
        ]
        for data in defaults:
            cls.objects.get_or_create(page_type=data['page_type'], defaults=data)