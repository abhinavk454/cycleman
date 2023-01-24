from rest_framework import generics
from .models import Cycle
from .serializers import CycleSerializer

"""
All Endpoint
"""


class AllCycleView(generics.ListCreateAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


"""
Solo Endpoint
"""


class SingleCycleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
