import django_filters

from .models import Client


class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Client
        fields = {
            "status": ["exact"],
            "country": ["exact"],
            "state": ["exact"],
            "city": ["exact"],
            "created_at": ["gte", "lte"],
        }