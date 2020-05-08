from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.homeView, name='home'),
    path('login/', LoginView.as_view() , name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
]