from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', CustomRegisterView.as_view(template_name='register.html'), name='register'),
]
