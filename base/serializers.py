from rest_framework import serializers
from .models import CustomUser, GroupOfUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupOfUser
        fields = '__all__'
