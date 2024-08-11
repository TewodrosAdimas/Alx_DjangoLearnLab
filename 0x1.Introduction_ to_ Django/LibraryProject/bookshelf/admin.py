from django.contrib import admin
from django.contrib import admin
from .models import Book

# Register your models here.
admin.ModelAdmin.register(Book)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ("publication_year")

admin.site.register(Book, BookAdmin)