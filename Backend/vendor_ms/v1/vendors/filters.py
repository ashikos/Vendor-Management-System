from django_filters import rest_framework as filters
from django.db.models import Q


class VendorFilter(filters.FilterSet):
    """Filtering Order list by Vendor."""
    code = filters.CharFilter(method='code_filter')


    def code_filter(self, queryset, name, value):
        """Method to filter order withrespect to vendor code."""
        query = Q(vendor_code__icontains=value)
        return queryset.filter(query)