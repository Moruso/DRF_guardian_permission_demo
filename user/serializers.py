from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class GroupChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
