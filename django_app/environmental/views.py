from django.shortcuts import render
from rest_framework.views import APIView
from .models import EnvironmentalProccess
from .serializers import *
from rest_framework.decorators import api_view


class LatestEnvironmentalProccesses(APIView):
    def get(self, request, format=None):
        environmental_proccess = EnvironmentalProccess.active.all()[0:10]
        serializer = LatestEnvironmentalProccessesSerializer(environmental_proccess)
        return serializer.data


@api_view(['POST'])
def create_environmental_proccess(request):
    pass