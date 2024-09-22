from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def get_feed(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(feed_posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

class LikePostView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id
            )
            return Response({'status': 'liked'})
        return Response({'status': 'already liked'}, status=400)

    def destroy(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=400)