from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import APIKey
from pprint import pprint
from .serializers import APIKeySerializer


# Create your views here.


class APIManagerView(APIView):
    def get(self, request, format=None):
        queryset = APIKey.objects.all()
        serializer = APIKeySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = APIKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True, 'api_key': serializer.data})
