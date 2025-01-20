# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs
from .serializers import ContactUsSerializer

class ContactUsView(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)

        if serializer.is_valid():
            # Save the contact form data to the database
            contact = serializer.save()

            # Send the email notification to admin
            send_mail(
                subject=f"New Contact Us Message from {contact.name}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nMessage: {contact.message}",
                from_email='info@aielinstitute.org',  # Sender email
                recipient_list=[settings.CONTACT_US_EMAIL],  # Admin email
                fail_silently=False,
            )

            # Return success response
            return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)

        # Return validation errors if form is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs
from .serializers import ContactUsSerializer
from rest_framework import status

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()  # Specify the queryset for the viewset
    serializer_class = ContactUsSerializer  # Specify the serializer

    def create(self, request, *args, **kwargs):
        """
        Override the create method to send an email when a new ContactUs form is submitted.
        """
        # Call the default create method to validate and save the data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Send the email notification to the admin
            send_mail(
                subject=f"New Contact Us Message from {contact.name}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nMessage: {contact.message}",
                from_email='info@aielinstitute.org',  # Sender email
                recipient_list=[settings.CONTACT_US_EMAIL],  # Admin email
                fail_silently=False,
            )

            # Return success response
            return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)

        # Return validation errors if form is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
