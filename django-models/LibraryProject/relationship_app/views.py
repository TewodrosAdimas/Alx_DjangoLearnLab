from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Book 
from .forms import BookForm
from .models import Library

# Function-Based View: List all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the list_books.html template with the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display details for a specific library
class LibraryDetailView(DetailView):
    # Specify the model to retrieve the data
    model = Library

    # Specify the template to be used
    template_name = 'relationship_app/library_detail.html'

    # Set the context object name
    context_object_name = 'library'

# Login view using Django's built-in LoginView
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using Django's built-in LogoutView
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view using Django's built-in UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.shortcuts import render, redirect

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
