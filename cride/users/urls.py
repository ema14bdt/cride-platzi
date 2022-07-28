"""Circles URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/logout/', UserLogoutAPIView.as_view(), name='logout'),
]