from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ["created_at", "updated_at"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
            "id": {"read_only": True},
        }

    def validate(self, data):
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("Email already exists")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

    def login(self, validated_data):
        user = authenticate(
            username=validated_data["username"], password=validated_data["password"]
        )
        token, _ = Token.objects.get_or_create(user=user)
        return validated_data
