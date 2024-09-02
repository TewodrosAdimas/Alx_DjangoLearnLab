from django.urls import path, include
from .views import BookViewSet, BookList
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Books', BookViewSet)

urlpatterns = [
    path("booklist", BookList.as_view()),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]