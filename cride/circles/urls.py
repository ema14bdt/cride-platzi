"""Circles URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views
from .views import memberships as membership_views


router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='circles')
router.register(
    r'circles/(?P<slug_name>[a-zA-Z0-9_-]+)/members',
    membership_views.MembershipViewSet, 
    basename='memberships'
)

urlpatterns = [
    path('', include(router.urls)),
]