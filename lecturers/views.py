"""
Lecturers Views
"""
from django.shortcuts import render, get_object_or_404
from .models import Lecturer


def lecturer_list(request):
    senior_lecturers = Lecturer.objects.filter(lecturer_type='senior', is_active=True)
    junior_lecturers = Lecturer.objects.filter(lecturer_type='junior', is_active=True)

    context = {
        'senior_lecturers': senior_lecturers,
        'junior_lecturers': junior_lecturers,
        'senior_count': senior_lecturers.count(),
        'junior_count': junior_lecturers.count(),
    }
    return render(request, 'lecturers/lecturer_list.html', context)


def lecturer_detail(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk, is_active=True)
    return render(request, 'lecturers/lecturer_detail.html', {'lecturer': lecturer})
