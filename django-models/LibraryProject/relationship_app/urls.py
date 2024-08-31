from django.urls import path
from . import views 
from .views import list_books, LibraryDetailView
from .views import UserLoginView, UserLogoutView, register
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # URL for the function-based view
    path('books/', list_books, name='list_books'),

    # URL for the class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    # User authentication URLs
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),   
]