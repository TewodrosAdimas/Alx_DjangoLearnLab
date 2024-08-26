from django.shortcuts import render
from .models import Librarian, Book, Author
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# Custom login view
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  
            return redirect('home')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Custom logout view
def custom_logout_view(request):
    logout(request)  
    return redirect('login') 

# Custom registration form
class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

# Custom registration view
def custom_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
