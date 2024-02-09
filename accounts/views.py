from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.response import Response


class RegisterUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    
    

class LoginUserView(APIView):
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = UserSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    ...