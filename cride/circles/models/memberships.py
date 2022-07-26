"""Membership model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Membership(CRideModel):
    """Membership model.
    
    A membership is the table that holds the relationship between
    a user and a circle
    """

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE
    )
    circle = models.ForeignKey(
        'circles.Circle',
        on_delete=models.CASCADE
    )

    is_admin = models.BooleanField(
        'circle admin',
        default=False,
        help_text="Circle admins can update the circle's data and manage its members."
    )

    # Invitation
    used_invitations = models.PositiveSmallIntegerField(
        default=0,
        help_text="Number of invitations used to join the circle."
    )
    remaining_invitations = models.PositiveSmallIntegerField(
        default=0,
        help_text="Number of invitations remaining to join the circle."
    )
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by',
        help_text="User that invited this user to the circle."
    )

    # Stats
    rides_taken = models.PositiveSmallIntegerField(default=0)
    rides_offered = models.PositiveSmallIntegerField(default=0)

    # Status
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text="Only active users are allowed to interact in the circle."
    )

    def __str__(self):
        """Return username and circle."""
        return f'{self.user.username} in {self.circle.slug_name}'

