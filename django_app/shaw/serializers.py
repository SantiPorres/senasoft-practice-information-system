from rest_framework import serializers
from .models import ShawProcess


class ShawProcessSerializer(serializers.Serializer):

    class Meta:
        models = ShawProcess

        fields = (
            'id',
            'sub_formation_area',
            'formation_environment',
            'title',
            'created_by',
            'created_at',
        )