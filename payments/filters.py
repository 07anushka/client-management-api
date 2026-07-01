import django_filters

from .models import Payment


class PaymentFilter(django_filters.FilterSet):

    class Meta:
        model = Payment

        fields = {
            "payment_status": ["exact"],
            "payment_method": ["exact"],
            "payment_date": ["gte", "lte"],
            "amount_paid": ["gte", "lte"],
        }