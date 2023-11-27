from django.db import models
from django.db import transaction

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from common.models import AbstractbaseModel

from v1.accounts.models import ProjectUser

# Create your models here.


class Vendor(AbstractbaseModel): 
    """
    Model to store details of vendors
        attributes
            name = CharField - Name of vendor
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

    name = models.CharField(default="", null=True, blank=True, max_length=150)
    contact_details = models.TextField(default="", null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    vendor_code = models.CharField(
        max_length=150, unique=True, blank=True, null=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.name}'
    

    def generate_vendor_code(self):
        """Function to generate vendor code"""

        try:
            previous_vendor = Vendor.objects.all().order_by("-id")[1]
        except:
            previous_vendor = None

        if previous_vendor:
            id = previous_vendor.vendor_code.split("-")[1]
            code = int(id) + 1
        else:
            code = 1000

        self.vendor_code = str(f"VEN-{code}")
        self.save()
        return self.vendor_code
    
    




class Perfomance(AbstractbaseModel):
    """
    models to store perfomance of vendors
        attributes
         vendor: ForeignKey - Vendor model.
         date: DateTimeField - Date of the performance record.
         on_time_delivery_rate: FloatField - record of the on-time delivery rate.
         quality_rating_avg: FloatField - ecord of the quality rating average.
         average_response_time: FloatField - record of the average response time.
         fulfillment_rate: FloatField - record of the fullfilment rate.
    """

    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="perfomance")
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate =  models.FloatField(null=True, blank=True)
    quality_rating_avg =  models.FloatField(null=True, blank=True)
    average_response_time =  models.FloatField(null=True, blank=True)
    fulfillment_rate =  models.FloatField(null=True, blank=True)

    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.first_name}-{self.last_name}'










