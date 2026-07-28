"""
School Pages URLs
"""
from django.urls import path
from . import views

urlpatterns = [
    path('vc/', views.vc_page, name='vc_page'),
    path('faculty/', views.faculty_page, name='faculty_page'),
    path('hod/', views.hod_page, name='hod_page'),
    path('ict/', views.ict_page, name='ict_page'),
    path('ippto/', views.ippto_page, name='ippto_page'),
]
