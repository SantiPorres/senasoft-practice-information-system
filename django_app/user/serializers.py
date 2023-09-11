from rest_framework import serializers
from .models import User

from rest_framework.serializers import raise_errors_on_nested_writes, model_meta, traceback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'personal_id_number',
            'first_name',
            'last_name',
            'password',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            personal_id_number=validated_data['personal_id_number'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
