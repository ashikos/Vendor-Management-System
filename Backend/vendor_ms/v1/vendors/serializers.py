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
        code = vendor.generate_vendor_code()
        
        return vendor

    