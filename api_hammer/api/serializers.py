from rest_framework import serializers

from users.models import User


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', 'password')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', 'invite_code')


class ActivitionInviteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', 'invite_code', 'activation')
