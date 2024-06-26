from rest_framework import generics, permissions, filters
from .models import DailyRoutine
from .serializers import DailyRoutineSerializer
from fitandfine_drf.permissions import IsOwnerOrReadOnly


class DailyRoutineList(generics.ListCreateAPIView):
    queryset = DailyRoutine.objects.all()
    serializer_class = DailyRoutineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['person_name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DailyRoutineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyRoutine.objects.all()
    serializer_class = DailyRoutineSerializer
    permission_classes = [IsOwnerOrReadOnly]
