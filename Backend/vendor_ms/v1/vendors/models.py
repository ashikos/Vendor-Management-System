from django.db import models
from django.db import transaction
from django.db.models import F, ExpressionWrapper, fields
from django.db.models import Sum, Count

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from common.models import AbstractbaseModel
from v1.orders.constants import StatusTypes

# Create your models here.


class Vendor(AbstractbaseModel): 
    """
    Model to store details of vendors
        attributes
            name = CharField - Name of vendor
            contact_details: TextField - Contact information of the vendor.
            address: TextField - Physical address of the vendor.
            vendor_code: CharField - A unique identifier for the vendor.
    """

    name = models.CharField(default="", null=True, blank=True, max_length=150)
    contact_details = models.TextField(default="", null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    vendor_code = models.CharField(
        max_length=150, unique=True, blank=True, null=True)

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
    

    def calculate_on_time_delivery_rate(self):
        """Function to calculate on time delivery rate of the vendor"""

        perfomance = self.perfomance.all().first()
        total_no_orders = self.orders.all().count()
        on_time_delivery_count = self.orders.filter(
            delivered_on__lte=F('expected_delivery_date')).count()
        
        if total_no_orders == 0:
            rate = 0 
        else:
            rate = (on_time_delivery_count/total_no_orders) * 100
        
        perfomance.on_time_delivery_rate = rate
        perfomance.save()
        return perfomance.on_time_delivery_rate
    

    def calculate_quality_rating(self):
        """Function to calculate the quality rating average """

        perfomance = self.perfomance.all().first()
        result = self.orders.all().aggregate(
            total_ratings=Sum("quality_rating"),
            total_count=Count("id")
        )

        if result["total_count"] == 0:
            avg = 0
        else:
            avg = (result["total_ratings"]/result["total_count"]) 

        perfomance.quality_rating_avg = avg
        perfomance.save()
        return perfomance.quality_rating_avg

    
    def calculate_average_response_time(self):
        """function to caluclate the average of time between issue_date and 
            acknowledgment_date
        """
        perfomance = self.perfomance.all().first()
        orders = self.orders.all()
        result = orders.annotate(
            time_difference=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField())).aggregate(total_time=Sum(
                    "time_difference"), order_count=Count("id"))
        
        
        if not result['total_time']:
            avg_time = None
        else:
            time_in_hrs = (result['total_time'].total_seconds()/3600)
            avg_time = time_in_hrs/result['order_count']

        perfomance.average_response_time = avg_time
        perfomance.save()
        return perfomance.average_response_time
    

    def calculate_fulfillment_rate(self):
        """function to caluclate the fulfillment_rate
        """
        perfomance = self.perfomance.all().first()
        total_orders = self.orders.all().count()
        successfull_orders = self.orders.filter(
            status=StatusTypes.Completed).count()
        
        fulfillment_rate = (successfull_orders/total_orders)*100

        perfomance.fulfillment_rate = fulfillment_rate
        perfomance.save()
        return perfomance.fulfillment_rate
        


class Perfomance(AbstractbaseModel):
    """
    models to store perfomance of vendors
        attributes
         vendor: ForeignKey - Vendor model.
         date: DateTimeField - Date of the performance record.
         on_time_delivery_rate: FloatField - record of the on-time delivery rate.
         quality_rating_avg: FloatField - record of the quality rating average.
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
        return f'{self.id}: {self.vendor.name}-{self.fulfillment_rate}'
    


