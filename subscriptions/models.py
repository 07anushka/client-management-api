from django.db import models

from clients.models import Client
from packages.models import Package


class ClientPackage(models.Model):

    STATUS = (
        ("active", "Active"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )

    start_date = models.DateField()

    end_date = models.DateField()

    renewal = models.BooleanField(default=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="active",
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.client.company_name} - {self.package.name}"