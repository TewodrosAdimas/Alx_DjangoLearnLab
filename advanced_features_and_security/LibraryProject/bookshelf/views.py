from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import books
from django.core.exceptions import PermissionDenied


# Create your views here.
@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_books(request, book_id):
    books = get_object_or_404(books, id=book_id)
    if request.method == 'POST':
        # Process form data and update the books
        form = booksForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=books.id)  # Redirect to the books detail view
    else:
        form = booksForm(instance=books)

    return render(request, 'your_app_name/edit_books.html', {'form': form})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_books(request, book_id):
    books = get_object_or_404(books, id=book_id)
    if request.method == 'POST':
        books.delete()
        return redirect('book_list')  # Redirect to the books list view after deletion

    return render(request, 'your_app_name/delete_books.html', {'books': books})


def custom_permission_denied_view(request, exception):
    return render(request, 'your_app_name/permission_denied.html', status=403)
