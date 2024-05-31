from django.urls import path
from .views import DailyRoutineList, DailyRoutineDetail

urlpatterns = [
    path(
        'dailyroutines/', 
        DailyRoutineList.as_view(), 
        name='daily-routine-list'
    ),
    path(
        'dailyroutines/<int:pk>/', 
        DailyRoutineDetail.as_view(), 
        name='daily-routine-detail'
    ),
]
