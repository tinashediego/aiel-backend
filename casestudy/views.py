from rest_framework import viewsets
from .models import CaseStudy
from .serializers import CaseStudySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
