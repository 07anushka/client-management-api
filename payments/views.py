import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter

logger = logging.getLogger(__name__)


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.select_related(
        "subscription",
        "subscription__client",
        "subscription__package",
    )

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    filterset_class = PaymentFilter

    search_fields = [
        "invoice_number",
        "subscription__client__company_name",
        "subscription__package__name",
    ]

    ordering_fields = "__all__"
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        logger.info(
            f"Payment '{serializer.validated_data['invoice_number']}' created by {self.request.user.username}"
        )
        serializer.save()

    def perform_update(self, serializer):
        logger.info(
            f"Payment '{serializer.instance.invoice_number}' updated by {self.request.user.username}"
        )
        serializer.save()

    def perform_destroy(self, instance):
        logger.info(
            f"Payment '{instance.invoice_number}' deleted by {self.request.user.username}"
        )
        instance.delete()