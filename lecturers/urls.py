"""
Lecturers URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecturer_list, name='lecturer_list'),
    path('<int:pk>/', views.lecturer_detail, name='lecturer_detail'),
]
