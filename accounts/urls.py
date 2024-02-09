from rest_framework.urls import path
from accounts.views import RegisterUserView, LoginUserView


app_name = 'accounts'

urlpatterns = [
    path('register', RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name="login"),
]