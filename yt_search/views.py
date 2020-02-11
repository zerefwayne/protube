from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import YoutubeVideo
# Create your views here.


class VideoView(viewsets.ModelViewSet):
    queryset = YoutubeVideo.objects.all()
    serializer_class = VideoSerializer
