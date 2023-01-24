from rest_framework import generics
from .models import Cycle
from .serializers import CycleSerializer


class AllCycleView(generics.ListCreateAPIView):
    '''All Endpoint'''
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class SingleCycleView(generics.RetrieveUpdateDestroyAPIView):
    '''Solo Endpoint'''
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
