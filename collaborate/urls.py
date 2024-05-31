from django.urls import path
from .views import AboutView, CollaborateListCreate, CollaborateDetail

urlpatterns = [
    path('about/',
         AboutView.as_view(),
         name='about'),
    path('collaborate/',
         CollaborateListCreate.as_view(),
         name='collaborate-list'),
    path('collaborate/<int:pk>/',
         CollaborateDetail.as_view(),
         name='collaborate-detail'),
]
