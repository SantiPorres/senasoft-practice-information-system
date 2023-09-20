from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest

from .models import EnvironmentalProcess
from .serializers import EnvironmentalProcessSerializer


class LatestEnvironmentalProcesses(APIView):
    def get(self, request, format=None):
        environmental_processes = EnvironmentalProcess.active.all()[0:10]

        print(environmental_processes)

        serializer = EnvironmentalProcessSerializer(environmental_processes, many=True)

        return Response(serializer.data)


class EnvironmentalProcessList(APIView):
    def get(self, request, format=None):
        environmental_processes = EnvironmentalProcess.active.all()
        serializer = EnvironmentalProcessSerializer(environmental_processes, many=True)

        return Response(serializer.data)
    

class EnvironmentalProcessDetail(APIView):
    def get(self, request, environmental_process_slug, format=None):
        environmental_process = EnvironmentalProcess.active.get(slug=environmental_process_slug)
        serializer = EnvironmentalProcessSerializer(environmental_process)

        return Response(serializer.data)


@api_view(['POST'])
def create_environmental_process(request):
    serializer = EnvironmentalProcessSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    EnvironmentalProcess.objects.create(request)
    return Response(
        {'message': 'Environmental process successfully created'},
        status=status.HTTP_201_CREATED
    )
