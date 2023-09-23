from rest_framework import serializers
from .models import User

from rest_framework.serializers import raise_errors_on_nested_writes, model_meta, traceback


class UserSerializer(serializers.Serializer):

    personal_id_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    mobile = serializers.CharField()
    email = serializers.CharField()

    group = serializers.CharField()

    """class Meta:
        model = User
        fields = [
            'personal_id_number',
            'first_name',
            'last_name',
            'password',
            'mobile',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}"""

    """def create(self, validated_data):
        user = User(
            personal_id_number=validated_data['personal_id_number'],
            email=validated_data['email'],
        )
        print(user)
        user.set_password(validated_data['password'])
        user.save()
        return user
"""