from rest_framework import serializers
from .models import CaseStudy

class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'
