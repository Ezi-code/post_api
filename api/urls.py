from django.urls import path, include
from core.views import *

urlpatterns = [
    path('posts', PostViewSets.as_view(), name='posts'),
    path('user', UserViewSets.as_view(), name='user'),
    path('user-create', CreateUserView.as_view(), name='create-user'),
    path('view-post', ViewPostView.as_view(), name='view-post'),
]

