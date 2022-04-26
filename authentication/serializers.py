from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        min_length=5, max_length=50, required=True)
    username = serializers.CharField(min_length=6, required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
