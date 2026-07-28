# """
# School Pages Views
# """
# from django.shortcuts import render, get_object_or_404
# from .models import SchoolPage


# def vc_page(request):
#     page = get_object_or_404(SchoolPage, page_type='vc', is_active=True)
#     return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Vice Chancellor'})


# def faculty_page(request):
#     page = get_object_or_404(SchoolPage, page_type='faculty', is_active=True)
#     return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Faculty of Science'})


# def hod_page(request):
#     page = get_object_or_404(SchoolPage, page_type='hod', is_active=True)
#     return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Head of Department'})


# def ict_page(request):
#     page = get_object_or_404(SchoolPage, page_type='ict', is_active=True)
#     return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Director of ICT'})
"""
School Pages Views
"""
from django.shortcuts import render, get_object_or_404
from .models import SchoolPage


def vc_page(request):
    page = get_object_or_404(SchoolPage, page_type='vc', is_active=True)
    return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Vice Chancellor'})


def faculty_page(request):
    page = get_object_or_404(SchoolPage, page_type='faculty', is_active=True)
    return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Faculty of Science'})


def hod_page(request):
    page = get_object_or_404(SchoolPage, page_type='hod', is_active=True)
    return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Head of Department'})


def ict_page(request):
    page = get_object_or_404(SchoolPage, page_type='ict', is_active=True)
    return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'Director of ICT'})


def ippto_page(request):
    page = get_object_or_404(SchoolPage, page_type='ippto', is_active=True)
    return render(request, 'school_pages/school_page.html', {'page': page, 'page_type': 'IPPTO Director'})