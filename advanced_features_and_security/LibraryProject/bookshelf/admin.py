from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser  # Import your custom user model

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add additional fields to the UserAdmin fieldsets and add_fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Specify fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth', 'profile_photo')

    # Add the fields to the search fields to make them searchable
    search_fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth')

# Register your custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
