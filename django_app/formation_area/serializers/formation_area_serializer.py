from rest_framework import serializers

from ..models.formation_area_model import FormationArea
from .sub_formation_area_serializer import SubFormationAreaSerializer


class FormationAreaSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=36)
    description = serializers.CharField(max_length=1000)

    sub_formation_areas = SubFormationAreaSerializer(many=True, read_only=True)

    class Meta:
        model = FormationArea
        fields = (
            "id",
            "name",
            "description",
            "slug",
            "status",
            "created_at",
            "updated_at",
            "get_absolute_url",
            "sub_formation_areas"
        )

        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'get_absolute_url',
            'sub_formation_areas',
        )
