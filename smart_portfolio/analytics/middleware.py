from .models import VisitorSession, CountryStats, DeviceInfo
from django.utils.timezone import now
import geoip2.database
import user_agents

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.geoip = geoip2.database.Reader('GeoLite2-Country.mmdb')  # Ensure this file is downloaded

    def __call__(self, request):
        response = self.get_response(request)
        ip = request.META.get("REMOTE_ADDR", "127.0.0.1")
        try:
            country = self.geoip.country(ip).country.name or "Unknown"
        except Exception:
            country = "Unknown"

        ua_string = request.META.get("HTTP_USER_AGENT", "")
        user_agent = user_agents.parse(ua_string)

        # Save a VisitorSession
        VisitorSession.objects.create(
            ip_address=ip,
            visited_url=request.path,
            timestamp=now(),
        )

        # Save Country
        CountryStats.objects.get_or_create(country=country)

        # Save device info
        DeviceInfo.objects.create(
            device_type="Mobile" if user_agent.is_mobile else "PC",
            browser=user_agent.browser.family,
            os=user_agent.os.family,
        )

        return response
