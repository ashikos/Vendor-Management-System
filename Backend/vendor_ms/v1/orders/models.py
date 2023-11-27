from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from v1.vendors.models import *
from common.models import AbstractbaseModel
from v1.orders.constants import StatusTypes

# Create your models here.


class Order(AbstractbaseModel): 
    """
    Model to store details of orders taken by vendors
        attributes
            po_number: CharField - Unique number identifying the PO.
            vendor: ForeignKey - Link to the Vendor model.
            order_date: DateTimeField - Date when the order was placed.
            delivery_date: DateTimeField - Expected or actual delivery date of the order.
            items: JSONField - Details of items ordered.
            quantity: IntegerField - Total quantity of items in the PO.
            status: CharField - Current status of the PO
            quality_rating: FloatField - Rating given to the vendor for this PO (nullable).
            issue_date: DateTimeField - Timestamp when the PO was issued to the vendor.
            acknowledgment_date: DateTimeField, nullable - Timestamp when the vendor acknowledged the PO.

    """

    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="orders")
    po_number = models.CharField(
        default="", max_length=100, null=True, blank=True, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.IntegerField(
        default=StatusTypes.Pending, choices=StatusTypes.choices())
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.vendor.first_name}-{self.po_number}'





