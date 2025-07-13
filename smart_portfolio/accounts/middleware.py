from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class JWTAuthWith2FA(JWTAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if result is None:
            return None
        user, _ = result
        if user.is_2fa_enabled and not request.session.get('2fa_verified'):
            raise PermissionDenied("2FA required")
        return user, _