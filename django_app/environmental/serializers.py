from rest_framework import serializers
from .models import EnvironmentalProcess


class EnvironmentalProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvironmentalProcess

        fields = (
            'id',
            'title',
            'date',
            'activity',
            'environmental_aspect',
            'impact',
            'impact_description',
            'recoverability',
            'classification',
            'nature',
            'observations',
            'slug',
            'get_formation_area_name',
            'get_sub_formation_area_name',
            'get_formation_environment_name',
            'created_by',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'slug',
            'created_by',
            'created_at',
            'updated_at',
        )