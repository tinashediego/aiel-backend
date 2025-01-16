from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'image', 'fullname', 'position', 'bio','linkedin_url','x_url','phone_number','email_address','created_at', 'updated_at']
