from rest_framework import serializers
from django.db import transaction

from v1.vendors import models




class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta info"""
        model =  models.Vendor
        fields = "__all__"

    @transaction.atomic()
    def create(self, validated_data):
        """
        create override for  the group object to update installment details
        """
        
        vendor = super().create(validated_data)
        vendor.generate_vendor_code()

        perfomance, created = models.Perfomance.objects.get_or_create(
            vendor=vendor)
        
        return vendor
    

class VendorPerfomanceSerializer(serializers.Serializer):
    # Define your serializer fields here if needed

    def to_representation(self, instance):

        perfomance = instance.perfomance.all().first()
        data = {
            "name": instance.name,
            "vendor_code": instance.vendor_code,
            "on_time_delivery_rate": perfomance.on_time_delivery_rate,
            "quality_rating_avg" :  perfomance.quality_rating_avg,
            "average_response_time" :  perfomance.average_response_time,
            "fulfillment_rate" :  perfomance.fulfillment_rate,
        }

        return data

    