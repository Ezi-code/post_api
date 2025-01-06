"""posts views."""

from .models import Post
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema

# VIEWSETS FOR POST MODLE


# view a single post
@extend_schema(responses={200: PostSerializer})
class ViewPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


@extend_schema(responses={200: PostSerializer})
class ViewPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# view single post object
@extend_schema(responses={200: PostSerializer})
class GetPostView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# update post
@extend_schema(responses={200: PostSerializer})
class UpdatePostView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [DjangoObjectPermissions]
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# delete post
class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# create post
@extend_schema(request=PostSerializer, responses={201: PostSerializer})
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


# search posts
@extend_schema(responses={200: PostSerializer})
class PostSearchView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["^title", "^description", "^author"]
