from rest_framework import viewsets

from django.shortcuts import render
from v1.orders import models as ord_models
from v1.orders import serializers as ord_serializers

# Create your views here.


class OrderView(viewsets.ModelViewSet):
    """ view of order"""

    queryset = ord_models.Order.objects.all()
    serializer_class = ord_serializers.OrderSerializer