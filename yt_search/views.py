from django.shortcuts import render
from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import YoutubeVideo
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from yt_pagination import YoutubeVideoResultsPagination


class VideoView(APIView, YoutubeVideoResultsPagination):

    def get(self, request, format=None):
        queryset = YoutubeVideo.objects.all()
        page = self.paginate_queryset(queryset, request)

        if page is not None:
            serializer = VideoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
