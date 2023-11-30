from django_filters import rest_framework as filters
from django.db.models import Q

from v1.orders import models as ord_models


class VendorFilter(filters.FilterSet):
    """Filtering Order list by Vendor."""
    vendor = filters.CharFilter(method='vendor_filter')
    po = filters.CharFilter(method='po_filter')
    v_code = filters.CharFilter(method='vendor_code_filter')


    def vendor_filter(self, queryset, name, value):
        """Method to filter order withrespect to vendor id."""
        query = Q(vendor__id=value)
        return queryset.filter(query)
    
    def po_filter(self, queryset, name, value):
        """Method to filter order withrespect to order po number."""
        query = Q(po_number__icontains=value)
        return queryset.filter(query)
    
    def vendor_code_filter(self, queryset, name, value):
        """Method to filter order withrespect to vendor code."""
        query = Q(vendor__vendor_code__icontains=value)
        return queryset.filter(query)




