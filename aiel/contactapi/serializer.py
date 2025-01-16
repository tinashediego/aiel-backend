from rest_framework import serializers

class ContactUsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    message = serializers.CharField(max_length=1000)
