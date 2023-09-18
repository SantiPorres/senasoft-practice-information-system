from django.http import HttpResponseBadRequest

from ..models import FormationEnvironment
from ..serializers import FormationEnvironmentSerializer

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils.views import GetObject,\
    check_if_sub_formation_area_exists_and_active,\
    check_if_formation_area_exists_and_active,\
    check_if_formation_environment_name_exists


class FormationEnvironmentList(APIView):
    def get(
            self, 
            request, 
            formation_area_slug, 
            sub_formation_area_slug, 
            format=None
        ):

        if formation_area_slug == None:
            return HttpResponseBadRequest
        
        if sub_formation_area_slug == None:
            return HttpResponseBadRequest
        
        if check_if_formation_area_exists_and_active(formation_area_slug) == False:
            return Response(
                {'detail': 'Unexisting formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if check_if_sub_formation_area_exists_and_active(sub_formation_area_slug) == False:
            return Response(
                {'detail': 'Unexisting sub_formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )

        GetObject().get_sub_formation_area_by_slug(formation_area_slug, sub_formation_area_slug)

        formation_environments = FormationEnvironment.active.filter(
            formation_area__slug=formation_area_slug,
            sub_formation_area__slug=sub_formation_area_slug,
        )
        serializer = FormationEnvironmentSerializer(
            formation_environments, 
            many=True
        )

        return Response(serializer.data)
    

class FormationEnvironmentDetail(APIView):
    def get(
            self, 
            request, 
            formation_area_slug, 
            sub_formation_area_slug, 
            formation_environment_slug, 
            format=None
        ):

        if check_if_formation_area_exists_and_active(formation_area_slug) == False:
            return Response(
                {'detail': 'Unexisting formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if check_if_sub_formation_area_exists_and_active(sub_formation_area_slug) == False:
            return Response(
                {'detail': 'Unexisting sub_formation_area.'},
                status=status.HTTP_404_NOT_FOUND
            )

        formation_environment = GetObject().get_formation_environment_by_slug(
            formation_area_slug, 
            sub_formation_area_slug,
            formation_environment_slug
        )
        serializer = FormationEnvironmentSerializer(formation_environment)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_formation_environment(
    request, 
    formation_area_slug_parameter,
    sub_formation_area_slug,
):

    serializer = FormationEnvironmentSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    
    if check_if_formation_area_exists_and_active(formation_area_slug_parameter) == False:
        return Response(
            {'detail': 'Unexisting formation_area.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if check_if_sub_formation_area_exists_and_active(sub_formation_area_slug) == False:
        return Response(
            {'detail': 'Unexisting sub_formation_area.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    sub_formation_area = GetObject().get_sub_formation_area_by_slug(
        formation_area_slug_parameter, 
        sub_formation_area_slug
    )

    formation_area_slug = sub_formation_area.get_formation_area_slug()

    if formation_area_slug_parameter != formation_area_slug:
        raise HttpResponseBadRequest
    
    formation_area = GetObject().get_formation_area_by_slug(formation_area_slug)
    
    if check_if_formation_environment_name_exists(request.data['name']):
        return Response(
            {'detail': 'formation_environment with this name already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    FormationEnvironment.objects.create(
        **serializer.validated_data, 
        formation_area=formation_area, 
        sub_formation_area=sub_formation_area
    )
    return Response(
        {'message': 'formation_environment successfully created'}, 
        status=status.HTTP_200_OK
    )
