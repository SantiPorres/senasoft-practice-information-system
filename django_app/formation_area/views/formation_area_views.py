from django.shortcuts import render
from django.http import Http404

from ..models import FormationArea
from ..serializers import FormationAreaSerializer, CreateFormationAreaSerializer

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.views import GetObject, check_if_formation_area_name_exists


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.objects.all()
        serializer = FormationAreaSerializer(formation_areas, many=True)

        return Response(serializer.data)
    

class FormationAreaDetail(APIView):
    def get(self, request, formation_area_slug, format=None):
        formation_area = GetObject().get_formation_area_by_slug(formation_area_slug)
        serializer = FormationAreaSerializer(formation_area)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_formation_area(request):
    serializer = CreateFormationAreaSerializer(data=request.data)

    if serializer.is_valid() == False:
        return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        if check_if_formation_area_name_exists(request.data['name']):
            return Response(
                {'detail': 'formation_area with this name already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            FormationArea.objects.create(**serializer.validated_data)
            return Response({'message': 'Formation area successfully created'}, status=status.HTTP_200_OK)
