from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import (
    VisitorSession,
    CountryStats,
    ErrorLog,
    DeviceInfo,
    PerformanceMetrics
)
from .serializers import (
    VisitorSessionSerializer,
    CountryStatsSerializer,
    ErrorLogSerializer,
    DeviceInfoSerializer,
    PerformanceMetricsSerializer
)

class VisitorSessionListView(generics.ListAPIView):
    queryset = VisitorSession.objects.all()
    serializer_class = VisitorSessionSerializer

class CountryStatsListView(generics.ListAPIView):
    queryset = CountryStats.objects.all()
    serializer_class = CountryStatsSerializer

class ErrorLogCreateView(generics.CreateAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer

class DeviceInfoCreateView(generics.CreateAPIView):
    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer

class PerformanceMetricsCreateView(generics.CreateAPIView):
    queryset = PerformanceMetrics.objects.all()
    serializer_class = PerformanceMetricsSerializer
