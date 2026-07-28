"""
Yearbook URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_yearbook, name='generate_yearbook'),
]
