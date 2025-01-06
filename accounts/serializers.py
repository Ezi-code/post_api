from rest_framework import serializers
from accounts.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return super().create(validated_data)
