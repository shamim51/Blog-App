from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom

from django.contrib.auth.models import User
#from django.dispatch import receiver
from .models import profile as pfl



# Create your views here.

"""def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect ('login')

    else:
        form = UserRegisterFrom()
        return render(request, 'users/register.html', {'form':form})"""
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            new_user = User.objects.all().last()
            new_user_profile = pfl.objects.create(user=new_user)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created successfully, Now you can Log In')
            return redirect('login')
    else:
        form = UserRegisterFrom()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render (request, 'users/profile.html')
