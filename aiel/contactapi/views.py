from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage

from aiel.contactapi.serializer import ContactUsSerializer


class ContactUsView(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            message = serializer.validated_data['message']

            try:
                # Create the email message
                email_message = EmailMessage(
                    subject=f"Contact Us Form Submission from {name}",
                    body=f"Name: {name}\nEmail: {email}\nEmail: {phone}\n\nMessage:\n{message}",
                    from_email='info@aielinstitute.org',  # Fixed sender email
                    to=['info@aielinstitute.org'],  # Your professional email
                    headers={'Reply-To': email}  # User's email for replies
                )
                # Send the email
                email_message.send(fail_silently=False)

                return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": "Failed to send the message. Please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
