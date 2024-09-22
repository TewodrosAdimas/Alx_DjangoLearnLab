from django.urls import path
from .views import CustomAuthToken
from . import views

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', UserListView.as_view(), name='user_list'),
]