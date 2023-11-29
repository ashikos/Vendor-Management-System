from v1.orders.constants import StatusTypes


def update_perfomance_data(instance, validated_data):
    """ updating vendor perfomance according to the order"""

    if "status" in validated_data.keys():
        status = validated_data["status"]
        # if status != instance.status:
        instance.vendor.calculate_fulfillment_rate()
        if (status == StatusTypes.Completed):
            instance.vendor.calculate_on_time_delivery_rate()

    if instance.quality_rating:
        instance.vendor.calculate_quality_rating()

    if instance.acknowledgment_date:
        instance.vendor.calculate_average_response_time()

    if instance.quality_rating:
        instance.vendor.calculate_fulfillment_rate()

    return instance