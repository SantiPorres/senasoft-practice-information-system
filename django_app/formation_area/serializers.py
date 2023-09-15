from .models import FormationArea, SubFormationArea, FormationEnvironment
from rest_framework import serializers


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


class CreateFormationAreaSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=36
    )

    description = serializers.CharField(
        max_length=1000
    )


class CreateSubFormationAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubFormationArea
        fields = (
            "name",
            "description",
            "formation_area",
            "status",
        )
