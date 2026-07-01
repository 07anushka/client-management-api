from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "invoice_number",
        "subscription",
        "total_amount",
        "amount_paid",
        "balance",
        "payment_status",
        "payment_method",
        "payment_date",
    )

    list_filter = (
        "payment_status",
        "payment_method",
    )

    search_fields = (
        "invoice_number",
        "subscription__client__company_name",
        "subscription__package__name",
    )

    ordering = (
        "-payment_date",
    )

    readonly_fields = (
        "balance",
    )

    list_per_page = 20