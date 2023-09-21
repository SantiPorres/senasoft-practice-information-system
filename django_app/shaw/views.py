from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ShawProcessSerializer
from .models import ShawProcess


class LatestShawProcesses(APIView):
    def get(self, request, format=None):
        shaw_process = ShawProcess.active.all()[0:10]
        serializer = ShawProcessSerializer(shaw_process)
        return serializer.data


class ShawProcessList(APIView):
    def get(self, request, format=None):
        shaw_processes = ShawProcess.active.all()
        serializer = ShawProcessSerializer(shaw_processes, many=True)

        return Response(serializer.data)
    

class ShawProcessDetail(APIView):
    def get(self, request, shaw_process_slug, format=None):
        shaw_process = ShawProcess.active.get(slug=shaw_process_slug)
        serializer = ShawProcessSerializer(shaw_process)

        return Response(serializer.data)