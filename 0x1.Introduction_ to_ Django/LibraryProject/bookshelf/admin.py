from django.contrib import admin
from django.contrib import admin
from .models import Book

# Register your models here.
admin.ModelAdmin.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)