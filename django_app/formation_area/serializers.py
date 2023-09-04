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
    formation_environments = FormationEnvironmentSerializer(many=True)

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
    sub_formation_areas = SubFormationAreaSerializer(many=True)

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

    class Meta:
        model = FormationArea
        fields = (
            "name",
            "description",
            "slug",
            "status",
        )


"""class FormationEnvironmentSerializer(serializers.ModelSerializer):

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

    class Meta:
        model = SubFormationArea
        fields = (
            "id",
            "name",
            "description",
            'formation_area_id',
            "slug",
            "status",
            "created_at",
            "updated_at",
            "get_absolute_url",
        )


class FormationAreaSerializer(serializers.ModelSerializer):

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
        )"""