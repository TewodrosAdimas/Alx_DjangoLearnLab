from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView 

path('accounts/', include('django.contrib.auth.urls')),path('accounts/profile/', 
         TemplateView.as_view(template_name='accounts/profile.html'), 
         name='profile'),path("signup/", 
         SignUpView.as_view(), 
         name="signup"),
