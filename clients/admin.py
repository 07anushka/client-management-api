from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "client_name",
        "email",
        "phone",
        "city",
        "country",
        "status",
        "created_at",
    )

    search_fields = (
        "company_name",
        "client_name",
        "email",
        "phone",
    )

    list_filter = (
        "status",
        "country",
        "city",
    )

    ordering = ("-created_at",)