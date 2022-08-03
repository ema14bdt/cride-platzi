"""Circles views."""

# Django REST Framework
from rest_framework import viewsets

# Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.circles import IsCircleAdmin

# Models
from cride.circles.models import Circle, Membership

# Serializers
from cride.circles.serializers import CircleModelSerializer


class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    serializer_class = CircleModelSerializer

    def get_queryset(self):
        """Return list to public-only."""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        """Assign permissions based on actions."""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign circle admin."""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )
        