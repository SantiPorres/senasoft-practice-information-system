from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import Group
from utils.constants import INSTRUCTORS_ROLE
from .serializers import UserSerializer
from .models import User


def add_to_instructor_group(request):
    try:
        instructors_group = Group.objects.get(name='instructors')
    except Group.DoesNotExist:
        raise Http404
    request.user.groups.add(instructors_group)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    group = Group.objects.filter(name=data.get('group'))
    print(group)
    del data['group']


    #self.groups.set([Group.objects.get(name='instructors')])

    user = User.objects.create(**data)

    user.groups.set(group)
    return Response(status.HTTP_201_CREATED)