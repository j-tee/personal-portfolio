# dashboard/urls.py
from django.urls import path
from .views import DashboardOverview

urlpatterns = [
    path('overview/', DashboardOverview.as_view(), name='dashboard-overview'),
]
