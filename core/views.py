"""
Core Views - Home, About, Contact
"""
from django.shortcuts import render
from django.contrib import messages
from students.models import Student
from lecturers.models import Lecturer
from school_pages.models import SchoolPage


def home(request):
    approved_students = Student.objects.filter(is_approved=True)[:6]
    senior_lecturers = Lecturer.objects.filter(lecturer_type='senior', is_active=True)[:4]
    junior_lecturers = Lecturer.objects.filter(lecturer_type='junior', is_active=True)[:4]
    
    # Changed from [:4] to [:5] to allow the IPPTO Director card to load
    school_pages = SchoolPage.objects.filter(is_active=True)[:5]

    context = {
        'approved_students': approved_students,
        'senior_lecturers': senior_lecturers,
        'junior_lecturers': junior_lecturers,
        'school_pages': school_pages,
        'student_count': Student.objects.filter(is_approved=True).count(),
        'lecturer_count': Lecturer.objects.filter(is_active=True).count(),
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
    return render(request, 'core/contact.html')
    
def school_overview(request):
    return render(request, 'school_overview.html')
