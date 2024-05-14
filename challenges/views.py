from rest_framework import generics, permissions
from .models import Challenge
from .serializers import ChallengeSerializer
from fitandfine_drf.permissions import IsOwnerOrReadOnly

class ChallengeList(generics.ListCreateAPIView):
    """
    List challenges or create a challenge if logged in.
    The perform_create method associates the challenge with the logged-in user.
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChallengeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a challenge, edit or delete it if you own it.
    Uses custom permissions to allow only the owner to modify or delete.
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsOwnerOrReadOnly]
