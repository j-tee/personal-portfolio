# analytics/models.py

from django.db import models
from django.utils import timezone


class VisitorSession(models.Model):
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=100, unique=True)
    user_agent = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Session {self.session_key} from {self.ip_address}"


class PageView(models.Model):
    session = models.ForeignKey(VisitorSession, on_delete=models.CASCADE, related_name='page_views')
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    referrer = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"View of {self.path} at {self.timestamp}"


class ClickEvent(models.Model):
    session = models.ForeignKey(VisitorSession, on_delete=models.CASCADE, related_name='clicks')
    element_id = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Click on {self.element_id} at {self.timestamp}"


class ContactFormEvent(models.Model):
    session = models.ForeignKey(VisitorSession, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"ContactForm by {self.name} at {self.submitted_at}"


class CountryStats(models.Model):
    ip_address = models.GenericIPAddressField()
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country_name} ({self.country_code}) at {self.timestamp}"
    
class ErrorLog(models.Model):
    level = models.CharField(max_length=50)  # e.g. "info", "warning", "error"
    message = models.TextField()
    stack_trace = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.level.upper()}] {self.path} at {self.timestamp}"
    
class DeviceInfo(models.Model):
    session = models.ForeignKey(VisitorSession, on_delete=models.CASCADE, related_name="devices")
    device_type = models.CharField(max_length=50)  # e.g. desktop, mobile, tablet
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    user_agent = models.TextField()
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_type} using {self.browser} on {self.os}"
    
class PerformanceMetrics(models.Model):
    session = models.ForeignKey(VisitorSession, on_delete=models.SET_NULL, null=True)
    path = models.CharField(max_length=255)
    load_time = models.FloatField(help_text="Page load time in milliseconds")
    api_latency = models.FloatField(null=True, blank=True, help_text="API latency in ms if applicable")
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Performance for {self.path} at {self.recorded_at}"
