import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Package
from .serializers import PackageSerializer
from .filters import PackageFilter

logger = logging.getLogger(__name__)


class PackageViewSet(viewsets.ModelViewSet):

    queryset = Package.objects.all()

    serializer_class = PackageSerializer

    permission_classes = [IsAuthenticated]

    filterset_class = PackageFilter

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = "__all__"

    ordering = ["-created_at"]

    def perform_create(self, serializer):

        logger.info(
            f"Package '{serializer.validated_data['name']}' created by {self.request.user.username}"
        )

        serializer.save()

    def perform_update(self, serializer):

        logger.info(
            f"Package '{serializer.instance.name}' updated by {self.request.user.username}"
        )

        serializer.save()

    def perform_destroy(self, instance):

        logger.info(
            f"Package '{instance.name}' deleted by {self.request.user.username}"
        )

        instance.delete()