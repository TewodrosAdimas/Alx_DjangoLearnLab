from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView, home
from django.contrib.auth.views import LoginView, LogoutView
from .views import profile_view
from django.contrib.auth.views import PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView




urlpatterns = [

    path('auth/', include('django.contrib.auth.urls')),
    path("register/", SignUpView.as_view(), name="register"),
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/profile/', profile_view, name='profileChange'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('accounts/profile/',
             TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path('post/', PostListView.as_view(), name='post_list'),                 # List all posts
    path('post/new/', PostCreateView.as_view(), name='post_create'),         # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),    # View a specific post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'), # Edit a specific post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:post_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('post/<int:post_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    
]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
