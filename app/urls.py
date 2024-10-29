from django.contrib import admin
from django.urls import path
# from app.view import hello, job_detail
# from . import views

from app import views

urlpatterns = [
    path('', views.job_list, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:job_id>', views.job_detail, name='jobs_detail'),
]