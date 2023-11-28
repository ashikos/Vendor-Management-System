from django.contrib import admin
from v1.orders.models import *

# Register your models here.

class OrderAdmin(admin.ModelAdmin):

    def get_vendor_name(self, obj):
        return obj.vendor.name

    list_display = (
        'get_vendor_name', "po_number", "order_date", "delivered_on", 
        "quality_rating" )


admin.site.register(Order, OrderAdmin)





