from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, remove_perm, get_groups_with_perms, get_users_with_perms
from goods.models import Good
from rest_framework import (
    permissions,
    status,
    viewsets,
)

from goods import serializers


# Create your views here.
class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GoodSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Good.objects.all()
    http_method_names = ['get', 'post', 'retrieve', ]

    permission_type = {'view': 'view_good',
                       'edit': 'change_good',
                       'deploy': 'deploy_good'
                       }

    def get_serializer_class(self):
        if self.action == 'add_permissions':
            return serializers.PermissionChoicesSerializer
        elif self.action == 'remove_permissions':
            return serializers.PermissionChoicesSerializer
        elif self.action == 'get_permission_users':
            return serializers.PermissionUserSerializer
        elif self.action == 'get_permission_users_2':
            return serializers.PermissionUserSerializer2
        elif self.action == 'get_permission_groups':
            return serializers.PermissionGroupSerializer
        elif self.action == 'get_permission_groups_2':
            return serializers.PermissionGroupSerializer2
        return self.serializer_class

    @action(['post'], detail=True)
    def add_permissions(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_or_group = []
            if serializer.data['users']:
                user_or_group.extend([User.objects.get(pk=u) for u in serializer.data['users']])
            if serializer.data['groups']:
                user_or_group.extend([Group.objects.get(pk=g) for g in serializer.data['groups']])
            for permission in serializer.data['permissions']:
                try:
                    assign_perm(self.permission_type.get(permission), user_or_group, good)
                except IntegrityError:
                    pass
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(['post'], detail=True)
    def remove_permissions(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_or_group = []
            if serializer.data['users']:
                user_or_group.extend([User.objects.get(pk=u) for u in serializer.data['users']])
            if serializer.data['groups']:
                user_or_group.extend([Group.objects.get(pk=g) for g in serializer.data['groups']])
            for permission in serializer.data['permissions']:
                for obj in user_or_group:
                    remove_perm(self.permission_type.get(permission), obj, good)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(['get'], detail=True)
    def get_permission_users(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        users = get_users_with_perms(good, attach_perms=True, with_group_users=False)
        serializer = self.get_serializer([{'id': u.id, 'name': u.username, 'pers': p} for u, p in users.items()],
                                         many=True)
        return Response(serializer.data)

    @action(['get'], detail=True)
    def get_permission_groups(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        groups = get_groups_with_perms(good, attach_perms=True)
        serializer = self.get_serializer([{'id': g.id, 'name': g.name, 'pers': p} for g, p in groups.items()],
                                         many=True)
        return Response(serializer.data)

    @action(['get'], detail=True)
    def get_permission_users_2(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        users = get_users_with_perms(good, with_group_users=False)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(['get'], detail=True)
    def get_permission_groups_2(self, request, pk=None, *args, **kwargs):
        queryset = Good.objects.all()
        good = get_object_or_404(queryset, pk=pk)
        groups = get_groups_with_perms(good)
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)
