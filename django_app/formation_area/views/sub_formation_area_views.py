from django.http import Http404

from ..models import SubFormationArea
from ..serializers import SubFormationAreaSerializer, CreateSubFormationAreaSerializer
from .views import GetObject

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class SubFormationAreaList(APIView):
    def get(self, request, formation_area_slug, format=None):
        sub_formation_areas = SubFormationArea.objects.filter(formation_area__slug=formation_area_slug)
        serializer = SubFormationAreaSerializer(sub_formation_areas, many=True)

        return Response(serializer.data)
    

class SubFormationAreaDetail(APIView):
    def get(self, request, formation_area_slug, sub_formation_area_slug, format=None):
        sub_formation_area = GetObject().get_sub_formation_area_by_slug(formation_area_slug, sub_formation_area_slug)
        serializer = SubFormationAreaSerializer(sub_formation_area)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_sub_formation_area(request):

    GetObject().get_formation_area_by_slug(request.data['formation_area'])

    if GetObject().get_sub_formation_area_by_name(
        request.data['formation_area'], 
        request.data['name']
    ):
        return Response(
            {'detail': 'sub_formation_area with this name already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = CreateSubFormationAreaSerializer(data=request.data)
    if serializer.is_valid():
        SubFormationArea.objects.create(**serializer.validated_data)
        return Response(
            {'message': 'Sub formation area successfully created'}, 
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
