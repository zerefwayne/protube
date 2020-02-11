from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import YoutubeVideo
from .tasks import add_two_numbers
# Create your views here.


class VideoView(viewsets.ModelViewSet):
    add_two_numbers.apply_async(countdown=10)
    queryset = YoutubeVideo.objects.all()
    serializer_class = VideoSerializer
