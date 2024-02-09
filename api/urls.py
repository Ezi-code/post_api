from django.urls import path, include
from core.views import *

app_name = 'api'

urlpatterns = [
    path('posts', ViewPostsView.as_view(), name='all-post'), 
    path('add-posts', CreatePostView.as_view(), name='view-post'), 
    path('delete-post/<int:pk>', DeletePostView.as_view(), name='view-post'), 
    path('update-post/<int:pk>', UpdatePostView.as_view(), name='create-post'),
    path('get-post/<int:pk>', GetPostView.as_view(), name='create-post'),
    
    path('create-user', CreateUserView.as_view(), name='create-user'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='create-user'),
    path('get-user/<int:pk>', ViewUserAPI.as_view(), name='create-user'),
    path('view-users', ViewAllUsers.as_view(), name="view_users"),
    # path('login', LoginUser.as_view())
]

