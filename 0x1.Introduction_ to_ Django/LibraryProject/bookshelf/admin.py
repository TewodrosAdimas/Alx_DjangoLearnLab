from django.contrib import admin
from django.contrib import admin
from .models import Book

# Register your models here.
admin.ModelAdmin.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date')

admin.site.register(Book, BookAdmin)