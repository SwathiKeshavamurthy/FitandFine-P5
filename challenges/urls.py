from django.urls import path
from .views import ChallengeList, ChallengeDetail, JoinChallenge, LeaveChallenge, UserChallenges

urlpatterns = [
    path('challenges/', ChallengeList.as_view(), name='challenge-list'),
    path('challenges/<int:pk>/', ChallengeDetail.as_view(), name='challenge-detail'),
    path('challenges/<int:pk>/join/', JoinChallenge.as_view(), name='join-challenge'),
    path('challenges/<int:pk>/leave/', LeaveChallenge.as_view(), name='leave-challenge'),
    path('my-challenges/', UserChallenges.as_view(), name='user-challenges'),
]
