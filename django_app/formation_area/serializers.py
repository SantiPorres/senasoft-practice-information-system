from .models import FormationArea, SubFormationArea, FormationEnvironment
from rest_framework import serializers


class FormationEnvironmentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=36)
    capacity = serializers.IntegerField(max_value=50)

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
            "get_formation_area_slug",
            "get_sub_formation_area_slug",
        )

        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'get_absolute_url',
            'get_formation_area_slug'
        )


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
