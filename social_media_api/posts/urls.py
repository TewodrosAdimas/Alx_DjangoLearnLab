from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import LikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed, name='feed'),
    path('<int:pk>/like/', LikePostView.as_view({'post': 'create'}), name='like_post'),
    path('<int:pk>/unlike/', LikePostView.as_view({'delete': 'destroy'}), name='unlike_post'),
]