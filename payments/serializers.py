from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    client = serializers.CharField(
        source="subscription.client.company_name",
        read_only=True
    )

    package = serializers.CharField(
        source="subscription.package.name",
        read_only=True
    )

    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = (
            "balance",
            "payment_status",
        )