from django.urls import path, include

from .views import APIManagerView

urlpatterns = [
    path('apikeys/', APIManagerView.as_view())
]
