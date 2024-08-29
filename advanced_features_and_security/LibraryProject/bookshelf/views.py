from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Book
from django.core.exceptions import PermissionDenied


# Create your views here.
@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Process form data and update the book
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Redirect to the book detail view
    else:
        form = BookForm(instance=book)

    return render(request, 'your_app_name/edit_book.html', {'form': form})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list view after deletion

    return render(request, 'your_app_name/delete_book.html', {'book': book})


def custom_permission_denied_view(request, exception):
    return render(request, 'your_app_name/permission_denied.html', status=403)
