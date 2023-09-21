from rest_framework import serializers
from .models import ShawProcess


class ShawProcessSerializer(serializers.Serializer):

    class Meta:
        models = ShawProcess

        fields = (
            'id',
            'title',
            'date',
            'danger_factor',
            'danger_source',
            'danger',
            'occupational_risk',
            'risk_source',
            'workers_exposed',
            'exposure_time',
            'occurrence_probability',
            'consequences',
            'danger_degree',
            'risk_degree',
            'danger_description',
            'created_by',
            'created_at',
            'updated_at',
        )

        read_only_fields = [
            'id',
            'slug',
            'created_at',
        ]