"""
Students Views
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Student
from .forms import StudentRegistrationForm, StudentProfileEditForm
from core.models import FormControl


def student_list(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(is_approved=True)

    if query:
        students = students.filter(
            Q(full_name__icontains=query) |
            Q(matric_number__icontains=query) |
            Q(bio__icontains=query) |
            Q(skills__icontains=query)
        )

    paginator = Paginator(students, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'total_students': students.count(),
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, is_approved=True)
    context = {
        'student': student,
        'skills_list': [s.strip() for s in student.skills.split(',') if s.strip()] if student.skills else [],
    }
    return render(request, 'students/student_detail.html', context)


@login_required
def student_register(request):
    form_control = FormControl.get_instance()
    if not form_control.is_registration_open():
        messages.error(request, 'Registration is currently closed.')
        return redirect('home')

    if hasattr(request.user, 'student_profile'):
        messages.info(request, 'You have already registered your profile.')
        return redirect('student_dashboard')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            messages.success(request, 'Your profile has been submitted for approval!')
            return redirect('student_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = StudentRegistrationForm()

    return render(request, 'students/student_register.html', {'form': form})


@login_required
def student_dashboard(request):
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        return redirect('student_register')

    context = {
        'student': student,
        'skills_list': [s.strip() for s in student.skills.split(',') if s.strip()] if student.skills else [],
    }
    return render(request, 'students/student_dashboard.html', context)


@login_required
def student_edit(request):
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        return redirect('student_register')

    if request.method == 'POST':
        form = StudentProfileEditForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('student_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = StudentProfileEditForm(instance=student)

    return render(request, 'students/student_edit.html', {'form': form, 'student': student})


def class_rep(request):
    try:
        class_rep_student = Student.objects.get(is_class_rep=True, is_approved=True)
    except Student.DoesNotExist:
        class_rep_student = None

    context = {
        'class_rep': class_rep_student,
    }
    return render(request, 'students/class_rep.html', context)
