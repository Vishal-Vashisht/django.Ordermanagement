from rest_framework import serializers
from apps.orders.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer"""

    class Meta:
        model = Orders
        fields = "__all__"

    def validate(self, attrs):
        if Orders.objects.filter(order_number=attrs["order_number"]).count() > 1:
            raise serializers.ValidationError({"order_number": "Order already exists"})
        return attrs


class OrderAggregateSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    total_orders = serializers.IntegerField()
    orders = OrderSerializer(many=True, allow_null=True)
