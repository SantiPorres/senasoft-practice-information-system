from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest

from .models import EnvironmentalProcess
from .serializers import EnvironmentalProcessSerializer

from utils.views import check_if_environmental_process_exists, check_if_environmental_process_unique_constraint_exists


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

    if check_if_environmental_process_unique_constraint_exists(request.data['title'], request.data['formation_environment']):
        return Response(
            {'message': 'An environmental process with this title already exists at this formation environment.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    EnvironmentalProcess.objects.create(request)
    return Response(
        {'message': 'Environmental process successfully created'},
        status=status.HTTP_201_CREATED
    )


@api_view(['DELETE'])
def delete_environmental_proccess(request, environmental_process_slug):
    
    if check_if_environmental_process_exists(environmental_process_slug) == False:
        return Response(
            {'message': 'That environmental process does not exist.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    environmental_process = EnvironmentalProcess.objects.get(slug=environmental_process_slug)
    
    environmental_process.delete()
    
    return Response(
        {'message': 'Environmental process successfully deleted'},
        status=status.HTTP_200_OK
    )
