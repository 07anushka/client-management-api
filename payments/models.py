from django.db import models

from subscriptions.models import ClientPackage


class Payment(models.Model):

    PAYMENT_METHODS = (
        ("cash", "Cash"),
        ("upi", "UPI"),
        ("card", "Card"),
        ("bank", "Bank Transfer"),
    )

    STATUS = (
        ("pending", "Pending"),
        ("partial", "Partial"),
        ("paid", "Paid"),
    )

    subscription = models.ForeignKey(
        ClientPackage,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    invoice_number = models.CharField(
        max_length=50,
        unique=True
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default="upi"
    )

    payment_status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pending"
    )

    payment_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.balance = self.total_amount - self.amount_paid

        if self.balance <= 0:
            self.payment_status = "paid"
        elif self.amount_paid > 0:
            self.payment_status = "partial"
        else:
            self.payment_status = "pending"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number