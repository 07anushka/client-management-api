import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ClientPackage
from .serializers import ClientPackageSerializer
from .filters import ClientPackageFilter

logger = logging.getLogger(__name__)


class ClientPackageViewSet(viewsets.ModelViewSet):

    queryset = ClientPackage.objects.select_related(
        "client",
        "package"
    )

    serializer_class = ClientPackageSerializer

    permission_classes = [IsAuthenticated]

    filterset_class = ClientPackageFilter

    search_fields = [
        "client__company_name",
        "package__name",
    ]

    ordering_fields = "__all__"

    ordering = ["-created_at"]

    def perform_create(self, serializer):

        logger.info(
            f"Package assigned by {self.request.user.username}"
        )

        serializer.save()

    def perform_update(self, serializer):

        logger.info(
            f"Subscription updated by {self.request.user.username}"
        )

        serializer.save()

    def perform_destroy(self, instance):

        logger.info(
            f"Subscription deleted by {self.request.user.username}"
        )

        instance.delete()