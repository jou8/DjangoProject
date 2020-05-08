from django.contrib import admin
from django.urls import path    
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('register', views.student_form, name='student_insert'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('<int:id>/', views.student_form, name='student_update'),
]
