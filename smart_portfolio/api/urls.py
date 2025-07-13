from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('analytics/', include('analytics.urls')),
    path('dashboard/', include('dashboard.urls')),
]
