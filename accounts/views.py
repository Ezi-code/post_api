from rest_framework import generics
from accounts.serializers import UserSerializer
from accounts.models import UserModel
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema

# VIEWSETS FOR USER MODEL


# Create a user account
@extend_schema(request=UserSerializer, responses=UserSerializer)
class CreateUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]


# Update a user account
@extend_schema(responses={200: UserSerializer})
class UpdateUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]


@extend_schema(responses={200: UserSerializer})
class ViewUserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]


# Delete a user accounts
class DeleteUserView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]


# get all registered Users
class ViewAllUsers(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
