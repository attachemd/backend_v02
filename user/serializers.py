from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from backend_v02 import settings


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6
            }
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['default_expired_time'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()
        # ...

        return token
