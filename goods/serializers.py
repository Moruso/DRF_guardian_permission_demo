from .models import Good
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from user.serializers import UserChoicesSerializer


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class PermissionChoicesSerializer(serializers.Serializer):
    default_error_messages = {'invalid_object': 'Group and user cannot both be empty'
                              }

    permissions = serializers.MultipleChoiceField(choices=['view', 'edit', 'deploy'])
    users = serializers.MultipleChoiceField(choices=[(u.id, u.username) for u in User.objects.all()], allow_blank=True)
    groups = serializers.MultipleChoiceField(choices=[(g.id, g.name) for g in Group.objects.all()], allow_blank=True)

    def validate(self, attrs):
        users = attrs.get('users', None)
        groups = attrs.get('groups', None)
        if users or groups:
            return attrs
        else:
            self.fail('invalid_object')


class PermissionUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    pers = serializers.ListField()


class PermissionGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    pers = serializers.CharField()


class PermissionUserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'userobjectpermission_set')
        depth = 2


class PermissionGroupSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'userobjectpermission_set')
        depth = 2

