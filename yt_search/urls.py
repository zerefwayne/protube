from django.urls import path, include

from .views import VideoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideoView)

urlpatterns = [
    path('', include(router.urls))
]

# AIzaSyAiXhiotgS4Ett0i5jsmk5VH_Nv-LUVH80

# https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&q=football&regionCode=IN&type=video&key=AIzaSyAiXhiotgS4Ett0i5jsmk5VH_Nv-LUVH80