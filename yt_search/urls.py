from django.urls import path, include

from .views import VideoView

urlpatterns = [
    path('videos/', VideoView.as_view())
]
