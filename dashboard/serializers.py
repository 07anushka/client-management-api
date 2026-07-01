from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    total_clients = serializers.IntegerField()
    active_clients = serializers.IntegerField()
    inactive_clients = serializers.IntegerField()

    total_packages = serializers.IntegerField()

    active_subscriptions = serializers.IntegerField()
    expired_subscriptions = serializers.IntegerField()

    total_projects = serializers.IntegerField()
    completed_projects = serializers.IntegerField()
    ongoing_projects = serializers.IntegerField()

    total_revenue = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    amount_received = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    pending_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )