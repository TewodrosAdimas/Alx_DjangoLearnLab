from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]