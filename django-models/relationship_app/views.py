from typing import Any
from django.shortcuts import render
from .models import Librarian, Book, Author
from .models import Library
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.



def BookList(request):
    all_books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", all_books)
class ListAllBooks(ListView):
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'  # Name to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library_name = "Central Library"
        context['library'] = Library.objects.get(name=library_name)
        # library = Library.objects.get(name=library_name)
        # context['books'] = library.books.all()       
        return context


class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')