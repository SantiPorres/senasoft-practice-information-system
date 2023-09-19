from rest_framework import serializers
from .models import EnvironmentalProcess


class EnvironmentalProcessSerializer(serializers.Serializer):

    class Meta:
        models = EnvironmentalProcess

        fields = (
            'id',
            'sub_formation_area',
            'formation_environment',
            'title',
            'created_by',
            'created_at',
        )