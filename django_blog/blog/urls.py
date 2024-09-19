from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView, home
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import profile_view
from django.contrib.auth.views import PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('auth/', include('django.contrib.auth.urls')),
    path("register/", SignUpView.as_view(), name="register"),
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/profile/', profile_view, name='profileChange'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('accounts/profile/',
             TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
