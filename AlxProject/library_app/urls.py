from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
