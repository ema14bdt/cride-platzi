"""Circles URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import UserSignUpAPIView, UserLoginAPIView, UserLogoutAPIView, AccountVerificationAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]