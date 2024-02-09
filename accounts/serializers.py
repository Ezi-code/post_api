from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password",)

    def create(self, validated_data):
        # User.set_password=validated_data["password"]
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)