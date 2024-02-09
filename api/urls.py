from django.urls import path, include
from core.views import *

app_name = 'api'

urlpatterns = [
    # post usrls 
    path('posts', ViewPostsView.as_view(), name='all-post'), 
    path('add-posts', CreatePostView.as_view(), name='view-post'), 
    path('delete-post/<int:pk>', DeletePostView.as_view(), name='view-post'), 
    path('update-post/<int:pk>', UpdatePostView.as_view(), name='create-post'),
    path('get-post/<int:pk>', GetPostView.as_view(), name='create-post'),
    path('search/', PostSearchView.as_view(), name="search"),
    
   
    # path('login', LoginUser.as_view())
]

