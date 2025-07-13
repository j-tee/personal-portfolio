# dashboard/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from portfolio.models import Project, Blog, Contact

class DashboardOverview(APIView):
    def get(self, request):
        return Response({
            "total_projects": Project.objects.count(),
            "total_blogs": Blog.objects.count(),
            "total_contacts": Contact.objects.count(),
            "latest_blogs": list(Blog.objects.order_by('-created_at')[:5].values()),
            "latest_contacts": list(Contact.objects.order_by('-created_at')[:5].values()),
        })
