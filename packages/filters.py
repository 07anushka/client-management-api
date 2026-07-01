import django_filters

from .models import Package


class PackageFilter(django_filters.FilterSet):

    class Meta:
        model = Package

        fields = {
            "status": ["exact"],
            "price": ["gte", "lte"],
            "duration_months": ["gte", "lte"],
        }