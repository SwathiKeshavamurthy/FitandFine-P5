from django.urls import path
from .views import ChallengeList, ChallengeDetail

urlpatterns = [
    path('challenges/', ChallengeList.as_view(), name='challenge-list'),
    path('challenges/<int:pk>/', ChallengeDetail.as_view(), name='challenge-detail'),
]
