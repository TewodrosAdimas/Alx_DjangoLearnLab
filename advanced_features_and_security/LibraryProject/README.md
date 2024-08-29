# Django Permissions and Groups Setup

## Overview

This README provides a guide to the setup and usage of custom permissions and user groups in the Django application. Permissions and groups are used to control access to various parts of the application, ensuring that users can only perform actions they are authorized to do.

## Custom Permissions

Custom permissions are defined in the `models.py` file within each model's `Meta` class. The following permissions have been added to the `Book` model:

- `can_view`: Permission to view book instances.
- `can_create`: Permission to create new book instances.
- `can_edit`: Permission to edit existing book instances.
- `can_delete`: Permission to delete book instances.

**Example: Custom Permissions in `models.py`**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
