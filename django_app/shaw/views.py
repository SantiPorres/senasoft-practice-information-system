from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import ShawProcessSerializer
from .models import ShawProcess


class LatestShawProcesses(APIView):
    def get(self, request, format=None):
        shaw_process = ShawProcess.active.all()[0:10]
        serializer = ShawProcessSerializer(shaw_process)
        return serializer.data
