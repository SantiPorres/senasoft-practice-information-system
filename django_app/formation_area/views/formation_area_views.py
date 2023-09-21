from ..models.formation_area_model import FormationArea
from ..serializers.formation_area_serializer import FormationAreaSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.views import GetObject, check_if_formation_area_name_exists, check_if_formation_area_exists


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.objects.all()
        serializer = FormationAreaSerializer(formation_areas, many=True)

        return Response(serializer.data)
    

class FormationAreaDetail(APIView):
    def get(self, request, formation_area_slug = None, format=None):
        formation_area = GetObject().get_formation_area_by_slug(formation_area_slug)
        serializer = FormationAreaSerializer(formation_area)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_formation_area(request):
    serializer = FormationAreaSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    if check_if_formation_area_name_exists(request.data['name']):
        return Response(
            {'message': 'formation_area with this name already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        FormationArea.objects.create(**serializer.validated_data)
        return Response(
            {'message': 'Formation area successfully created'}, 
            status=status.HTTP_201_CREATED
        )


@api_view(['DELETE'])
def delete_formation_area(request, formation_area_slug):
    if check_if_formation_area_exists(formation_area_slug) == False:
        return Response(
            {'message': 'This formation area does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    formation_area = FormationArea.objects.get(
        slug=formation_area_slug
    )

    formation_area.delete()

    return Response(
        {'message': 'Formation area successfully deleted'},
        status=status.HTTP_200_OK
    )
