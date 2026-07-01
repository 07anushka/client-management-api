from rest_framework import serializers

from .models import ClientPackage


class ClientPackageSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(
        source="client.company_name",
        read_only=True
    )

    package_name = serializers.CharField(
        source="package.name",
        read_only=True
    )

    class Meta:
        model = ClientPackage
        fields = "__all__"