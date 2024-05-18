from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Challenge, ChallengeParticipant
from .serializers import ChallengeSerializer, ChallengeParticipantSerializer
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

class JoinChallenge(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        challenge = generics.get_object_or_404(Challenge, pk=pk)
        ChallengeParticipant.objects.get_or_create(challenge=challenge, user=request.user)
        return Response(status=status.HTTP_201_CREATED)

class LeaveChallenge(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        challenge = generics.get_object_or_404(Challenge, pk=pk)
        participant = ChallengeParticipant.objects.filter(challenge=challenge, user=request.user)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserChallenges(generics.ListAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Challenge.objects.filter(challengeparticipant__user=user)
