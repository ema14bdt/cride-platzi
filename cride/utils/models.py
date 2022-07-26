"""Django models utilities."""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the objects was created
        + modified (DateTime): Store the last datetime the objects was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add = True, # When the object is created, set 'created' to now
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now = True, # When the object is saved, set 'modified' to now
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True # This model is an abstract base class

        get_latest_by = 'created' # Order by 'created' descending
        ordering = ['-created', '-modified'] # Order by 'created' descending, then 'modified' descending