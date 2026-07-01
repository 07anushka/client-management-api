from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(
        source="client.company_name",
        read_only=True
    )

    package_name = serializers.CharField(
        source="subscription.package.name",
        read_only=True
    )

    assigned_to_name = serializers.CharField(
        source="assigned_to.username",
        read_only=True
    )

    class Meta:
        model = Project
        fields = "__all__"