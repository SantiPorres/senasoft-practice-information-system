from rest_framework import serializers

from ..models.sub_formation_area_model import SubFormationArea
from .formation_environment_serializer import FormationEnvironmentSerializer


class SubFormationAreaSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=36)
    description = serializers.CharField(max_length=1000)

    formation_environments = FormationEnvironmentSerializer(many=True, read_only=True)

    class Meta:
        model = SubFormationArea
        fields = (
            "id",
            "name",
            "description",
            "slug",
            "status",
            "created_at",
            "updated_at",
            "get_absolute_url",
            "get_formation_area_slug",
            "formation_environments"
        )

        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'get_absolute_url',
            'get_formation_area_slug',
            'formation_environments',
        )
