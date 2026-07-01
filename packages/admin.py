from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "duration_months",
        "created_at",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20