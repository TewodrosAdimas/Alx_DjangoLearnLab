from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView
from .import views
from .views import list_books, LibraryDetailView
from .views import login, register, logout


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
