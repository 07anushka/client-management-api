from django.db import models

from clients.models import Client
from subscriptions.models import ClientPackage
from accounts.models import User


class Project(models.Model):

    STATUS_CHOICES = (
        ("not_started", "Not Started"),
        ("in_progress", "In Progress"),
        ("on_hold", "On Hold"),
        ("completed", "Completed"),
    )

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    subscription = models.ForeignKey(
        ClientPackage,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    project_name = models.CharField(max_length=255)

    description = models.TextField()

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    start_date = models.DateField()

    deadline = models.DateField()

    progress = models.PositiveIntegerField(default=0)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="not_started"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.project_name