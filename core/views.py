from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import generics

class PostViewSets(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permision_classes = [DjangoObjectPermissions]

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [DjangoObjectPermissions]

class UserViewSets(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ViewPostView(generics.ListAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    

# class PostViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def patch(self, request):
#         post = Post.objects.get(id=request.data['id'])
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
        

#     def delete(self, request):
#         post = Post.objects.get(id=request.data['id'])
#         if not post:
#             post.delete()
#             return Response('Post deleted')
#         return Response({
#             "status": False,
#             "message":"Post not found"
#         })


# class UserViewSets(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def patch(self, resquest):
#         data = resquest.data
#         objs = User.objects.filter(id=data['id']).first()
#         serializer = UserSerializer(objs, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)