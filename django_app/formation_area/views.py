from django.shortcuts import render
from .models import FormationArea, SubFormationArea, FormationEnvironment
from .serializers import FormationAreaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.objects.all()
        serializer = FormationAreaSerializer(formation_areas, many=True)

        return Response(serializer.data)
