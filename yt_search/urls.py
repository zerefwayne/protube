from django.urls import path, include

from .views import VideoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideoView)

urlpatterns = [
    path('', include(router.urls))
]
