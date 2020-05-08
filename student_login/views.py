from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def homeView(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count':count})
    
   
def loginView(request):
    return redirect(request, 'registration/login.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()   
    return render(request, 'registration/register.html',{'form':form})


def logoutView(request):
    return redirect('home')


