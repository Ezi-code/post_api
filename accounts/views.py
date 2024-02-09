from rest_framework import generics
from accounts.serializers import UserSerializer
from accounts.models import UserModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 

# VIEWSETS FOR USER MODEL

# Create a user account
class CreateUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    # authentication_classes = [TokenAuthentication]
    permission_classes = []  # [DjangoModelPermissionsOrAnonReadOnly]

# Update a user account
class UpdateUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# View a single user account 
class ViewUserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]


# Delete a user accounts 
class DeleteUserView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



# get all registered Users 
class ViewAllUsers(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    