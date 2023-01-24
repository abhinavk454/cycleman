from rest_framework import serializers

from .models import Cycle


class CycleSerializer(serializers.ModelSerializer):
    """Class Serializer"""

    class Meta:
        model = Cycle
        fields = ["id", "name", "edition", "price"]
