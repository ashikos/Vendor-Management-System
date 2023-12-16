from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from v1.vendors import models as ven_models
from v1.vendors import serializers as ven_serializers
from v1.accounts import permissions
from v1.vendors import filters as ven_filters

# Create your views here.


class  VendorView(viewsets.ModelViewSet):
    """views for vendors"""

    queryset = ven_models.Vendor.objects.all()
    serializer_class = ven_serializers.VendorSerializer
    filter_class = ven_filters.VendorFilter
    # permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None, **args):
        """function to return the perfomance of the vendor"""
        
        vendor = self.get_object()
        serializer = ven_serializers.VendorPerfomanceSerializer(vendor)

        return Response(serializer.data)


