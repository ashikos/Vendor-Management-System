from django.contrib import admin
from v1.vendors.models import *

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', )


class PerfomanceAdmin(admin.ModelAdmin):

    def get_vendor_name(self, obj):
        return obj.vendor.name

    list_display = (
        'get_vendor_name', "on_time_delivery_rate", "quality_rating_avg", 
        "average_response_time", "fulfillment_rate" )


admin.site.register(Vendor, VendorAdmin)
admin.site.register(Perfomance, PerfomanceAdmin)
