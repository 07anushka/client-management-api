import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Client
from .serializers import ClientSerializer
from .filters import ClientFilter

logger = logging.getLogger(__name__)


class ClientViewSet(viewsets.ModelViewSet):
    """
    Client CRUD API
    """

    queryset = Client.objects.filter(is_deleted=False)
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    # Filters
    filterset_class = ClientFilter

    # Search
    search_fields = [
        "company_name",
        "client_name",
        "email",
        "phone",
        "city",
        "state",
        "country",
    ]

    # Ordering
    ordering_fields = "__all__"
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        logger.info(
            f"Client '{serializer.validated_data['company_name']}' created by {self.request.user.username}"
        )

        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        logger.info(
            f"Client '{serializer.instance.company_name}' updated by {self.request.user.username}"
        )

        serializer.save(
            updated_by=self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            f"Client '{instance.company_name}' deleted by {self.request.user.username}"
        )

        instance.is_deleted = True
        instance.save()