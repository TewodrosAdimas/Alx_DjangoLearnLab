from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Comment
from .models import Post


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Add any additional fields you want to allow users to edit

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags field

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('The title must be at least 5 characters long.')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('The content must be at least 10 characters long.')
        return content

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        # Optionally validate tags if needed (e.g., check for duplicates)
        return tags




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Include only the content field for the comment

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize widget attributes if needed
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Add your comment here...',
            'rows': 4,
            'class': 'comment-textarea',  
        })

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("This field cannot be empty.")
        return content