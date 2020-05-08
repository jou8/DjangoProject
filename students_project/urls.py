from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('student_login.urls')),
    path('student/', include ('student_register.urls')),
    path('admin/', admin.site.urls),
]
