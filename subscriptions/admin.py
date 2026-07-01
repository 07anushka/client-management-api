from django.contrib import admin

from .models import ClientPackage


@admin.register(ClientPackage)
class ClientPackageAdmin(admin.ModelAdmin):

    list_display = (
        "client",
        "package",
        "start_date",
        "end_date",
        "status",
    )

    search_fields = (
        "client__company_name",
        "package__name",
    )

    list_filter = (
        "status",
        "renewal",
    )