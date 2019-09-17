from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from guardian.shortcuts import get_objects_for_user, get_objects_for_group

from rest_framework import (
    permissions,
    status,
    viewsets,
)

from user import serializers


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'retrieve', ]

    # @action(['post'], detail=True)
    # def add_permissions(self, request, pk=None, *args, **kwargs):
    #
    #     return Response(status=status.HTTP_200_OK)

    # @action(['post'], detail=True)
    # def remove_permissions(self, request, pk=None, *args, **kwargs):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #
    #     return Response(status=status.HTTP_200_OK)

    # @action(['get'], detail=True)
    # def get_user_permissions(self, request, pk=None, *args, **kwargs):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     get_objects_for_user(user, )
    #     return Response(status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Group.objects.all()
    http_method_names = ['get', 'post', 'retrieve', ]

    # @action(['post'], detail=True)
    # def add_permissions(self, request, pk=None, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)
    #
    # @action(['post'], detail=True)
    # def remove_permissions(self, request, pk=None, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)
