from rest_framework.urls import path
from accounts.views import CreateUserView, UpdateUserView, ViewAllUsers, ViewUserAPI


app_name = 'accounts'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create-user'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='create-user'),
    path('get-user/<int:pk>', ViewUserAPI.as_view(), name='create-user'),
    path('all-users/', ViewAllUsers.as_view(), name="view_users"),
]
