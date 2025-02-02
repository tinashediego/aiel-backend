from rest_framework import viewsets
from .models import ResearchHighlight
from .serializers import ResearchHighlightSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class ResearchHighlightViewSet(viewsets.ModelViewSet):
    queryset = ResearchHighlight.objects.all()
    serializer_class = ResearchHighlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
