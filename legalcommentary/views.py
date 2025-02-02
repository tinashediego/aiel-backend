from rest_framework import viewsets
from .models import LegalCommentary
from .serializers import LegalCommentarySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class LegalCommentaryViewSet(viewsets.ModelViewSet):
    queryset = LegalCommentary.objects.all()
    serializer_class = LegalCommentarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
