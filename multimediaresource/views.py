from rest_framework import viewsets
from .models import MultimediaResource
from .serializers import MultimedaiResourceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class MultimediaResourceViewSet(viewsets.ModelViewSet):
    queryset = MultimediaResource.objects.all()
    serializer_class = MultimedaiResourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
