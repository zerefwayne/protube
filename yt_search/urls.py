from django.urls import path, include

from .views import get_videos

urlpatterns = [
    path('videos/', get_videos)
]
