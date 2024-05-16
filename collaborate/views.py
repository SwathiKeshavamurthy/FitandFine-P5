from rest_framework import generics
from .models import About, Collaborate
from .serializers import AboutSerializer, CollaborateSerializer

class AboutView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update the About page content.
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = []  # Adjust based on your needs

class CollaborateListCreate(generics.ListCreateAPIView):
    """
    List all collaboration requests or create a new one.
    Allows any visitor to create or view collaboration requests.
    """
    queryset = Collaborate.objects.all()
    serializer_class = CollaborateSerializer
    permission_classes = []  # Open access

class CollaborateDetail(generics.RetrieveAPIView):
    """
    Retrieve a collaboration request.
    Allows any visitor to view collaboration requests.
    """
    queryset = Collaborate.objects.all()
    serializer_class = CollaborateSerializer
    permission_classes = []
