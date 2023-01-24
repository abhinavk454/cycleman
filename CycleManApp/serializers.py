from .models import Cycle
from rest_framework import serializers


class CycleSerializer(serializers.ModelSerializer):
    """Class Serializer"""

    class Meta:
        model = Cycle
        fields = ['id', 'name', 'edition', 'price']
