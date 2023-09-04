from django.shortcuts import render
from django.http import Http404

from .models import FormationArea, SubFormationArea, FormationEnvironment
from .serializers import FormationAreaSerializer, SubFormationAreaSerializer, FormationEnvironmentSerializer, CreateFormationAreaSerializer

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.objects.all()
        serializer = FormationAreaSerializer(formation_areas, many=True)

        return Response(serializer.data)
    

class FormationAreaDetail(APIView):
    def get_object(self, formation_area_slug):
        try:
            return FormationArea.objects.get(slug=formation_area_slug)
        except FormationArea.DoesNotExist:
            raise Http404

    def get(self, request, formation_area_slug, format=None):
        formation_area = self.get_object(formation_area_slug)
        serializer = FormationAreaSerializer(formation_area)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateFormationAreaSerializer(data=request.data)
        if serializer.is_valid():
            FormationArea.objects.create(**serializer.validated_data)
            return Response({'message': 'Formation Area created'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""class FormationAreaViewSet(viewsets.ModelViewSet):
    queryset = FormationArea.objects.all()
    serializer_class = FormationAreaSerializer

class SubFormationAreaViewSet(viewsets.ModelViewSet):
    queryset = SubFormationArea.objects.all()
    serializer_class = FormationAreaSerializer

class FormationEnvironmentViewSet(viewsets.ModelViewSet):
    queryset = FormationEnvironment.objects.all()
    serializer_class = FormationEnvironmentSerializer"""