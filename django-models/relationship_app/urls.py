from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView
from .import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', CustomRegisterView.as_view(template_name='register.html'), name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

]
