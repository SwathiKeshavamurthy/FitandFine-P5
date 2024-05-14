from rest_framework import generics, permissions
from .models import DailyRoutine
from .serializers import DailyRoutineSerializer
from fitandfine_drf.permissions import IsOwnerOrReadOnly

class DailyRoutineList(generics.ListCreateAPIView):
    queryset = DailyRoutine.objects.all()
    serializer_class = DailyRoutineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DailyRoutineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyRoutine.objects.all()
    serializer_class = DailyRoutineSerializer
    permission_classes = [IsOwnerOrReadOnly]
