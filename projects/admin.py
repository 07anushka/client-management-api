from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_name",
        "client",
        "assigned_to",
        "priority",
        "status",
        "progress",
    )

    list_filter = (
        "status",
        "priority",
    )

    search_fields = (
        "project_name",
        "client__company_name",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "status",
        "progress",
    )