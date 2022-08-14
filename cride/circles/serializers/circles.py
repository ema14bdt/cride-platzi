"""Circle serializers."""

 # Django REST Framework
from rest_framework import serializers

# Models
from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000,
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        model = Circle
        fields = (
            'name',
            'slug_name',
            'about',
            'picture',
            'rides_offered',
            'rides_taken',
            'verified',
            'is_public',
            'is_limited',
            'members_limit',
        )
        read_only_fields = (
            'rides_offered',
            'rides_taken',
            'verified',
            'is_limited',
        )

    def validate(self, data): # sobreescribimos el metodo validate
        """Ensure both members_limit and is_limited are present."""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False )
        if is_limited ^ bool(members_limit): # ^ es el xor
            raise serializers.ValidationError('If circle is limited, it must have a members limit.')
        return data
        