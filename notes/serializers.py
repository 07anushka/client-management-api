from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(
        source="client.company_name",
        read_only=True
    )

    created_by_name = serializers.CharField(
        source="created_by.username",
        read_only=True
    )

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = (
            "created_by",
            "created_at",
            "updated_at",
        )