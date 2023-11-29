from rest_framework import serializers
from django.db import transaction

from v1.orders import models as ord_models
from v1.orders import utils





class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        """class to store meta details"""
        model = ord_models.Order
        fields = "__all__"

    
    @transaction.atomic()
    def create(self, validated_data):

        """ create override to generate po_number for order and to update 
            vendor perfomance """
        
        order = super().create(validated_data)
        order.generate_po_number()

        vendor = utils.update_perfomance_data(order, validated_data)

        return order
    
    def update(self, instance, validated_data):
        """ Override update to update the perfomance of vendor """

        order = super().update(instance, validated_data)
        vendor = utils.update_perfomance_data(instance, validated_data)

        return order
        

    