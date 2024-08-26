from django.shortcuts import render
from .models import Librarian, Book, Author
from .models import Library
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('home')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def custom_logout_view(request):
    auth_logout(request)  
    return redirect('login')  
