from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import YoutubeVideo
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_videos(request):
    if request.method == 'GET':
        queryset = YoutubeVideo.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
