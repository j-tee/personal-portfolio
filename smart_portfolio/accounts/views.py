from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User, UserRegisterSerializer
from django.core.mail import send_mail
from django.urls import reverse
from .utils import verification_token
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
import pyotp
from django.conf import settings

class Enable2FAView(APIView):
    def post(self, request):
        user = request.user
        if not user.is_2fa_enabled:
            totp = pyotp.TOTP(user.otp_secret)
            provisioning_uri = totp.provisioning_uri(user.email, issuer_name="Smart Portfolio")
            return Response({"uri": provisioning_uri})  # Frontend shows QR code
        return Response({"error": "2FA already enabled"}, status=400)

class Verify2FAView(APIView):
    def post(self, request):
        user = request.user
        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(request.data.get('code')):
            user.is_2fa_enabled = True
            user.save()
            return Response({"message": "2FA enabled!"})
        return Response({"error": "Invalid code"}, status=400)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Send verification email (Step 3)
            return Response({"message": "User created! Verify email."})
        return Response(serializer.errors, status=400)
    
    
# def send_verification_email(user):
#     token = verification_token.make_token(user)
#     uid = urlsafe_base64_encode(force_str(user.pk).encode())
#     link = f"http://yourdomain.com{reverse('verify-email')}?uid={uid}&token={token}"
#     send_mail(
#         'Verify Your Email',
#         f'Click here: {link}',
#         'noreply@yourdomain.com',
#         [user.email],
#     )
def send_verification_email(user):
    token = verification_token.make_token(user)
    uid = urlsafe_base64_encode(force_str(user.pk).encode())
    
    # Read from .env via settings.py
    domain = settings.DOMAIN  # e.g., 'https://yourdomain.com'
    from_email = settings.DEFAULT_FROM_EMAIL  # e.g., 'noreply@yourdomain.com'
    
    verification_path = reverse('verify-email')
    link = f"{domain}{verification_path}?uid={uid}&token={token}"
    
    send_mail(
        'Verify Your Email',
        f'Click here to verify: {link}',
        from_email,
        [user.email],
        fail_silently=False,
    )
class VerifyEmailView(APIView):
    def get(self, request):
        uid = request.GET.get('uid')
        token = request.GET.get('token')
        try:
            user = User.objects.get(pk=force_str(urlsafe_base64_decode(uid)))
            if verification_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"message": "Email verified!"})
        except:
            pass
        return Response({"error": "Invalid link"}, status=400)