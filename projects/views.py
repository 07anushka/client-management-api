import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer
from .filters import ProjectFilter

logger = logging.getLogger(__name__)


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.select_related(
        "client",
        "subscription",
        "assigned_to",
    )

    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated]

    filterset_class = ProjectFilter

    search_fields = [
        "project_name",
        "client__company_name",
    ]

    ordering_fields = "__all__"

    ordering = ["-created_at"]

    def perform_create(self, serializer):
        logger.info(
            f"Project '{serializer.validated_data['project_name']}' created by {self.request.user.username}"
        )
        serializer.save()

    def perform_update(self, serializer):
        logger.info(
            f"Project '{serializer.instance.project_name}' updated by {self.request.user.username}"
        )
        serializer.save()

    def perform_destroy(self, instance):
        logger.info(
            f"Project '{instance.project_name}' deleted by {self.request.user.username}"
        )
        instance.delete()