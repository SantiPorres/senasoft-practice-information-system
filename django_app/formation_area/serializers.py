from .models import FormationArea, SubFormationArea, FormationEnvironment
from rest_framework import serializers

from utils.views import GetObject


class FormationEnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormationEnvironment
        fields = (
            "id",
            "name",
            "capacity",
            "slug",
            "status",
            "created_at",
            "updated_at",
            "get_absolute_url",
        )

        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'get_absolute_url',
        )


class SubFormationAreaSerializer(serializers.ModelSerializer):
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
            "formation_environments"
        )

        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'get_absolute_url',
            'formation_environments',
        )


class FormationAreaSerializer(serializers.ModelSerializer):
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
