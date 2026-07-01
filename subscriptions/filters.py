import django_filters

from .models import ClientPackage


class ClientPackageFilter(django_filters.FilterSet):

    class Meta:
        model = ClientPackage

        fields = {
            "status": ["exact"],
            "renewal": ["exact"],
            "start_date": ["gte", "lte"],
            "end_date": ["gte", "lte"],
        }