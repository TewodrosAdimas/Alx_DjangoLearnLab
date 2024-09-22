from django import forms
from taggit.models import Tag

class TagWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, str):
            # If value is a string, use it directly
            tags = value
        else:
            # Otherwise, assume value is a list of Tag instances
            tags = ', '.join(tag.name for tag in value or [])

        # Render the widget with tags as a comma-separated string
        return forms.TextInput(attrs={'value': tags}).render(name, tags, attrs, renderer)

    def value_from_form(self, data, files, name):
        # Convert the comma-separated string to a list of Tag names
        if data.get(name):
            tag_names = data[name].split(',')
            return [Tag.objects.get_or_create(name=tag_name.strip())[0] for tag_name in tag_names]
        return []