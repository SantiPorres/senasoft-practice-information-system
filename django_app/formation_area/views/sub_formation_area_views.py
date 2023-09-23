from django.http import HttpResponseBadRequest

from ..models.sub_formation_area_model import SubFormationArea
from ..serializers.sub_formation_area_serializer import SubFormationAreaSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.views import GetObject, check_if_sub_formation_area_name_exists, \
    check_if_formation_area_exists_and_active, check_if_sub_formation_area_exists


class SubFormationAreaList(APIView):
    def get(
            self, 
            request, 
            formation_area_slug, 
            format=None
        ):

        if formation_area_slug == None:
            return HttpResponseBadRequest

        if check_if_formation_area_exists_and_active(formation_area_slug) == False:
            return Response(
                {'message': 'Unexisting formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )

        sub_formation_areas = SubFormationArea.objects.filter(
            formation_area__slug=formation_area_slug
        )
        serializer = SubFormationAreaSerializer(sub_formation_areas, many=True)

        return Response(serializer.data)
    

class SubFormationAreaDetail(APIView):
    def get(self, request, formation_area_slug, sub_formation_area_slug, format=None):

        if check_if_formation_area_exists_and_active(formation_area_slug) == False:
            return Response(
                {'message': 'Unexisting formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )

        sub_formation_area = GetObject().get_sub_formation_area_by_slug(
            formation_area_slug, 
            sub_formation_area_slug
        )
        serializer = SubFormationAreaSerializer(sub_formation_area)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_sub_formation_area(request, formation_area_slug):

    serializer = SubFormationAreaSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    
    if check_if_formation_area_exists_and_active(formation_area_slug) == False:
        return Response(
            {'message': 'Unexisting formation_area.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    formation_area = GetObject().get_formation_area_by_slug(formation_area_slug)
    
    if check_if_sub_formation_area_name_exists(request.data['name']):
        return Response(
            {'message': 'sub_formation_area with this name already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    SubFormationArea.objects.create(**serializer.validated_data, formation_area=formation_area)
    return Response(
        {'message': 'sub_formation_area successfully created'}, 
        status=status.HTTP_201_CREATED
    )


@api_view(['DELETE'])
def delete_sub_formation_area(request, sub_formation_area_slug):
    if check_if_sub_formation_area_exists(sub_formation_area_slug) == False:
        return Response(
            {'message': 'This sub formation area does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    sub_formation_area = SubFormationArea.objects.get(
        slug=sub_formation_area_slug
    )

    sub_formation_area.delete()

    return Response(
        {'message': 'Sub formation area successfully deleted'},
        status=status.HTTP_200_OK
    )
