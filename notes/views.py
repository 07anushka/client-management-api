import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import NoteSerializer

logger = logging.getLogger(__name__)


class NoteViewSet(viewsets.ModelViewSet):

    queryset = Note.objects.select_related(
        "client",
        "created_by",
    )

    serializer_class = NoteSerializer

    permission_classes = [IsAuthenticated]

    search_fields = [
        "title",
        "description",
        "client__company_name",
    ]

    ordering_fields = "__all__"

    ordering = ["-created_at"]

    def perform_create(self, serializer):
        logger.info(
            f"Note '{serializer.validated_data['title']}' created by {self.request.user.username}"
        )

        serializer.save(
            created_by=self.request.user
        )

    def perform_update(self, serializer):
        logger.info(
            f"Note '{serializer.instance.title}' updated by {self.request.user.username}"
        )

        serializer.save()

    def perform_destroy(self, instance):
        logger.info(
            f"Note '{instance.title}' deleted by {self.request.user.username}"
        )

        instance.delete()