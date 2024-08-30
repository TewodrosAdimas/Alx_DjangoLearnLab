from django.shortcuts import render, get_object_or_404
from .models import Library

def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
