from django.urls import path
from .views import RegisterView
from .views import VerifyEmailView
from .views import Enable2FAView
from .views import Verify2FAView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("enable-2fa/", Enable2FAView.as_view(), name="enable-2fa"),
    path("verify-2fa/", Verify2FAView.as_view(), name="verify-2fa"),
]
