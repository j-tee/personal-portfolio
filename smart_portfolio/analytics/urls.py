from django.urls import path
from .views import (
		VisitorSessionListView,
		CountryStatsListView,
		ErrorLogCreateView,
		DeviceInfoCreateView,
		PerformanceMetricsCreateView
)
urlpatterns = [
     path("visitors/", VisitorSessionListView.as_view(), name="visitor-sessions"),
    path("countries/", CountryStatsListView.as_view(), name="country-stats"),
    path("errors/", ErrorLogCreateView.as_view(), name="error-logs"),
    path("devices/", DeviceInfoCreateView.as_view(), name="device-info"),
    path("performance/", PerformanceMetricsCreateView.as_view(), name="performance-metrics"),

]