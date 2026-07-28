"""
Students URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('register/', views.student_register, name='student_register'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('edit/', views.student_edit, name='student_edit'),
    path('class-rep/', views.class_rep, name='class_rep'),
]
