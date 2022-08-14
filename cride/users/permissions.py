"""Users permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to account owner."""

    def has_object_permission(self, request, view, obj):
        """Check if user is account owner."""
        return request.user == obj
        