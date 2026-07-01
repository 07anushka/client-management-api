from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = (
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
            "is_deleted",
        )