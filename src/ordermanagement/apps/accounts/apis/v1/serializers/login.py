from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    authenticate,
)


class LoginSerializer(serializers.Serializer):
    """Login Serializer."""
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get("username"),
            password=attrs.get("password"),
        )

        if not user:
            raise serializers.ValidationError({
                "email": "Invalid credentials"
            })

        if not user.is_active:
            raise serializers.ValidationError({
                "email": "Please activate you account"
            })

        attrs["user"] = user
        return attrs
