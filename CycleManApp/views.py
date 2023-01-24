from rest_framework import generics
from .models import Cycle
from .serializers import CycleSerializer


class AllCycleView(generics.ListCreateAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class SingleCycleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
