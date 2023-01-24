from .models import Cycle
from rest_framework import serializers

"""
Serializer
"""


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ['id', 'name', 'edition', 'price']
