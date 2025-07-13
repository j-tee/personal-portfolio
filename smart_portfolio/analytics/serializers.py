from rest_framework import serializers
from .models import (
    VisitorSession,
    CountryStats,
    ErrorLog,
    DeviceInfo,
    PerformanceMetrics,
)


class VisitorSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorSession
        fields = '__all__'


class CountryStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryStats
        fields = '__all__'


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'


class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = '__all__'


class PerformanceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMetrics
        fields = '__all__'
