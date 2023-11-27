from django.shortcuts import render
from rest_framework import viewsets

from v1.vendors import models as ven_models
from v1.vendors import serializers as ven_serializers

# Create your views here.


class  VendorView(viewsets.ModelViewSet):
    """views for vendors"""

    queryset = ven_models.Vendor.objects.all()
    serializer_class = ven_serializers.VendorSerializer
