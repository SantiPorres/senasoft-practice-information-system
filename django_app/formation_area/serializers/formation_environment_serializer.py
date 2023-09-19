from rest_framework import serializers

from ..models.formation_environment_model import FormationEnvironment


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
