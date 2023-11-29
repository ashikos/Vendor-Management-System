from django.db import models
from django.db.models import F

from common.models import AbstractbaseModel
from common.library import encode, decode

from v1.vendors.models import *
from v1.orders.constants import StatusTypes

# Create your models here.


class Order(AbstractbaseModel): 
    """
    Model to store details of orders taken by vendors
        attributes
            po_number: CharField - Unique number identifying the PO.
            vendor: ForeignKey - Link to the Vendor model.
            order_date: DateTimeField - Date when the order was placed.
            delivery_date: DateTimeField - Expected or actual delivery date 
                                                            of the order.
            items: JSONField - Details of items ordered.
            quantity: IntegerField - Total quantity of items in the PO.
            status: CharField - Current status of the PO
            quality_rating: FloatField - Rating given to the vendor for this PO.
            issue_date: DateTimeField - Timestamp when the PO was issued to the vendor.
            acknowledgment_date: DateTimeField, nullable - Timestamp when the 
                                                    vendor acknowledged the PO.

    """

    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="orders", 
        null=True, blank=True)
    po_number = models.CharField(
        default="", max_length=100, null=True, blank=True, unique=True)
    order_date = models.DateTimeField(null=True, blank=True)
    expected_delivery_date = models.DateTimeField(null=True, blank=True)
    delivered_on = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    status = models.IntegerField(
        default=StatusTypes.Pending, choices=StatusTypes.choices())
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def default_items():
        return {}
    
    items = models.JSONField(default=default_items, null=True, blank=True)


    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.vendor.name}-{self.po_number}'
    

    
    def generate_po_number(self):
        """Function to generate unique po_code for every order"""

        try:
            previous_order = Order.objects.all().order_by("-id")[1]
        except:
            previous_order = None

        if previous_order:
            code = decode(previous_order.po_number)
            code = code + 1
        else:
            code = 1000

        self.po_number = encode(code)
        self.save()
        return self




