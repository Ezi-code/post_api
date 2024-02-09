from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Post
from .serializer import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


# VIEWSETS FOR POST MODLE 

#view a single post
class ViewPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permision_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# view all posts 
class ViewPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]




# view single post object
class GetPostView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


#update post 
class UpdatePostView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [DjangoObjectPermissions]
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# delete post
class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# create post
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


# search posts 
class PostSearchView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', '^description', '^author']



