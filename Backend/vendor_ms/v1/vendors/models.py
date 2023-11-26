from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from v1.accounts.models import ProjectUser

# Create your models here.


class Vendor(ProjectUser): 
    """
    Model to store details of vendors
        attributes
            contact_details: TextField - Contact information of the vendor.
            address: TextField - Physical address of the vendor.
            vendor_code: CharField - A unique identifier for the vendor.
            on_time_delivery_rate: FloatField - Tracks the percentage of 
                                        on-time deliveries.
            quality_rating_avg: FloatField - Average rating of quality 
                                        based on purchase orders.
            average_response_time: FloatField - Average time taken to 
                                        acknowledge purchase orders.
            fulfillment_rate: FloatField - Percentage of purchase orders 
                                        fulfilled successfully.
    """

    contact_details = models.TextField(default="", null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    vendor_code = models.CharField(
        max_length=150, unique=True, blank=True, null=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)


