from rest_framework import serializers
from .models import MultimediaResource

class MultimedaiResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaResource
        fields = '__all__'
