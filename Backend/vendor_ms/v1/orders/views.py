from rest_framework import viewsets
from django_filters import rest_framework as filters

from django.shortcuts import render
from v1.orders import models as ord_models
from v1.orders import serializers as ord_serializers
from v1.accounts import permissions
from v1.orders import filters as ord_filters


# Create your views here.


class OrderView(viewsets.ModelViewSet):
    """
    View for managing orders. POST, GET, PATCH, DELETE 

    Attributes:
        queryset (QuerySet): The set of orders to be displayed.
        filter_class (FilterSet): The filter class used for filtering orders.
        serializer_class (Serializer): The serializer class for orders.
        permission_classes (list): The list of permissions required for accessing the view.

    CREATE :
        POST request to:
        `/api/orders/`

    RETRIVE :
        GET request to:
        `/api/orders/` or `/api/orders/<>`

    CREATE :
        POST request to:
        `/api/orders/`

    CREATE :
        POST request to:
        `/api/orders/`
    """

    queryset = ord_models.Order.objects.all()
    filter_class = ord_filters.VendorFilter
    serializer_class = ord_serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    