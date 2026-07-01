from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .serializers import DashboardSerializer

from clients.models import Client
from packages.models import Package
from subscriptions.models import ClientPackage
from payments.models import Payment
from projects.models import Project


@extend_schema(
    summary="Dashboard Statistics",
    description="Returns dashboard analytics including clients, packages, subscriptions, projects, and revenue statistics.",
    responses=DashboardSerializer,
)
class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_clients = Client.objects.filter(
            is_deleted=False
        ).count()

        active_clients = Client.objects.filter(
            status="active",
            is_deleted=False
        ).count()

        inactive_clients = Client.objects.filter(
            status="inactive",
            is_deleted=False
        ).count()

        total_packages = Package.objects.count()

        active_subscriptions = ClientPackage.objects.filter(
            status="active"
        ).count()

        expired_subscriptions = ClientPackage.objects.filter(
            status="expired"
        ).count()

        total_projects = Project.objects.count()

        completed_projects = Project.objects.filter(
            status="completed"
        ).count()

        ongoing_projects = Project.objects.filter(
            status="in_progress"
        ).count()

        payments = Payment.objects.all()

        total_revenue = sum(
            (payment.total_amount for payment in payments),
            Decimal("0.00")
        )

        amount_received = sum(
            (payment.amount_paid for payment in payments),
            Decimal("0.00")
        )

        pending_amount = sum(
            (payment.balance for payment in payments),
            Decimal("0.00")
        )

        return Response({
            "total_clients": total_clients,
            "active_clients": active_clients,
            "inactive_clients": inactive_clients,

            "total_packages": total_packages,

            "active_subscriptions": active_subscriptions,
            "expired_subscriptions": expired_subscriptions,

            "total_projects": total_projects,
            "completed_projects": completed_projects,
            "ongoing_projects": ongoing_projects,

            "total_revenue": total_revenue,
            "amount_received": amount_received,
            "pending_amount": pending_amount,
        })