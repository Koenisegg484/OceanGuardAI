from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaFileViewSet, get_processed_file

router = DefaultRouter()
router.register(r'media', MediaFileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('processed/<str:filename>/', get_processed_file, name='get_processed_file'),
]
