"""
Admin Portal Views
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator
from students.models import Student
from lecturers.models import Lecturer
from school_pages.models import SchoolPage
from core.models import FormControl, SiteSettings
from .forms import LecturerForm, SchoolPageForm, FormControlForm, SiteSettingsForm, StudentStatusForm


def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser or getattr(user, 'role', '') == 'admin')


@login_required
@user_passes_test(is_admin)
def dashboard(request):
    total_students = Student.objects.count()
    approved_students = Student.objects.filter(is_approved=True).count()
    pending_students = Student.objects.filter(is_approved=False).count()
    total_lecturers = Lecturer.objects.count()
    senior_lecturers = Lecturer.objects.filter(lecturer_type='senior').count()
    junior_lecturers = Lecturer.objects.filter(lecturer_type='junior').count()

    recent_students = Student.objects.order_by('-created_at')[:5]
    recent_lecturers = Lecturer.objects.order_by('-created_at')[:5]

    context = {
        'total_students': total_students,
        'approved_students': approved_students,
        'pending_students': pending_students,
        'total_lecturers': total_lecturers,
        'senior_lecturers': senior_lecturers,
        'junior_lecturers': junior_lecturers,
        'recent_students': recent_students,
        'recent_lecturers': recent_lecturers,
    }
    return render(request, 'admin_portal/dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def student_management(request):
    status = request.GET.get('status', 'all')
    query = request.GET.get('q', '')

    students = Student.objects.all().order_by('-created_at')

    if status == 'approved':
        students = students.filter(is_approved=True)
    elif status == 'pending':
        students = students.filter(is_approved=False)

    if query:
        students = students.filter(
            Q(full_name__icontains=query) |
            Q(matric_number__icontains=query) |
            Q(email__icontains=query)
        )

    paginator = Paginator(students, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'status': status,
        'query': query,
        'approved_count': Student.objects.filter(is_approved=True).count(),
        'pending_count': Student.objects.filter(is_approved=False).count(),
    }
    return render(request, 'admin_portal/student_management.html', context)


@login_required
@user_passes_test(is_admin)
def approve_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_approved = True
    student.save()
    messages.success(request, f'{student.full_name} has been approved.')
    return redirect('admin_students')


@login_required
@user_passes_test(is_admin)
def reject_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_approved = False
    student.save()
    messages.info(request, f'{student.full_name} has been rejected.')
    return redirect('admin_students')


@login_required
@user_passes_test(is_admin)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    name = student.full_name
    student.delete()
    messages.warning(request, f'{name} has been deleted.')
    return redirect('admin_students')


@login_required
@user_passes_test(is_admin)
def lecturer_management(request):
    lec_type = request.GET.get('type', 'all')
    query = request.GET.get('q', '')

    lecturers = Lecturer.objects.all().order_by('order', 'full_name')

    if lec_type == 'senior':
        lecturers = lecturers.filter(lecturer_type='senior')
    elif lec_type == 'junior':
        lecturers = lecturers.filter(lecturer_type='junior')

    if query:
        lecturers = lecturers.filter(Q(full_name__icontains=query) | Q(title__icontains=query))

    paginator = Paginator(lecturers, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'lec_type': lec_type,
        'query': query,
        'senior_count': Lecturer.objects.filter(lecturer_type='senior').count(),
        'junior_count': Lecturer.objects.filter(lecturer_type='junior').count(),
    }
    return render(request, 'admin_portal/lecturer_management.html', context)


@login_required
@user_passes_test(is_admin)
def add_lecturer(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lecturer added successfully!')
            return redirect('admin_lecturers')
    else:
        form = LecturerForm()
    return render(request, 'admin_portal/lecturer_form.html', {'form': form, 'action': 'Add'})


@login_required
@user_passes_test(is_admin)
def edit_lecturer(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST, request.FILES, instance=lecturer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lecturer updated successfully!')
            return redirect('admin_lecturers')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'admin_portal/lecturer_form.html', {'form': form, 'lecturer': lecturer, 'action': 'Edit'})


@login_required
@user_passes_test(is_admin)
def delete_lecturer(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    name = lecturer.full_name
    lecturer.delete()
    messages.warning(request, f'Lecturer {name} has been deleted.')
    return redirect('admin_lecturers')


@login_required
@user_passes_test(is_admin)
def school_management(request):
    pages = SchoolPage.objects.all().order_by('order')
    return render(request, 'admin_portal/school_management.html', {'pages': pages})


@login_required
@user_passes_test(is_admin)
def edit_school_page(request, page_type):
    page = get_object_or_404(SchoolPage, page_type=page_type)
    if request.method == 'POST':
        form = SchoolPageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, f'{page.get_page_type_display()} page updated!')
            return redirect('admin_school')
    else:
        form = SchoolPageForm(instance=page)
    return render(request, 'admin_portal/school_form.html', {'form': form, 'page': page})


@login_required
@user_passes_test(is_admin)
def form_control(request):
    control = FormControl.get_instance()
    if request.method == 'POST':
        form = FormControlForm(request.POST, instance=control)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form control settings updated!')
            return redirect('admin_form_control')
    else:
        form = FormControlForm(instance=control)
    return render(request, 'admin_portal/form_control.html', {'form': form, 'control': control})


@login_required
@user_passes_test(is_admin)
def site_settings_view(request):
    settings = SiteSettings.get_instance()
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Site settings updated!')
            return redirect('admin_settings')
    else:
        form = SiteSettingsForm(instance=settings)
    return render(request, 'admin_portal/site_settings.html', {'form': form, 'settings': settings})
