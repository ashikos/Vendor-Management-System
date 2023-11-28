from rest_framework import serializers
from v1.orders import models as ord_models
from django.db import transaction


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        """class to store meta details"""
        model = ord_models.Order
        fields = "__all__"

    
    @transaction.atomic()
    def create(self, validated_data):
        """
        create override for  the group object to update installment details
        """
        order = super().create(validated_data)
        order.generate_po_number()

        return order
        

    