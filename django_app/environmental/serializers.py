from rest_framework import serializers
from .models import EnvironmentalProccess


class LatestEnvironmentalProccessesSerializer(serializers.Serializer):

    class Meta:
        models = EnvironmentalProccess

        fields = (
            'id',
            'sub_formation_area',
            'formation_environment',
            'title',
            'created_by',
            'created_at',
        )