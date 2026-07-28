"""
Admin Portal URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('students/', views.student_management, name='admin_students'),
    path('students/approve/<int:pk>/', views.approve_student, name='admin_approve_student'),
    path('students/reject/<int:pk>/', views.reject_student, name='admin_reject_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='admin_delete_student'),
    path('lecturers/', views.lecturer_management, name='admin_lecturers'),
    path('lecturers/add/', views.add_lecturer, name='admin_add_lecturer'),
    path('lecturers/edit/<int:pk>/', views.edit_lecturer, name='admin_edit_lecturer'),
    path('lecturers/delete/<int:pk>/', views.delete_lecturer, name='admin_delete_lecturer'),
    path('school/', views.school_management, name='admin_school'),
    path('school/edit/<str:page_type>/', views.edit_school_page, name='admin_edit_school'),
    path('form-control/', views.form_control, name='admin_form_control'),
    path('settings/', views.site_settings_view, name='admin_settings'),
]
