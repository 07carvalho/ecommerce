from rest_framework import serializers
from .models import Order, OrderAddress, OrderItem


class OrderAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderAddress
        exclude = ('user',)


class OrderItemResumeSerializer(serializers.ModelSerializer):
    """Return Products instances only with relevant fields to the Cart context"""
    class Meta:
        model = OrderItem
        exclude = ('order',)


class OrderSerializer(serializers.ModelSerializer):

    address = OrderAddressSerializer()
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Order
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context['user']
        address = validated_data.pop('address')
        return Order().make_order(user=user, address=address)

    def get_items(self, obj):
        return OrderItemResumeSerializer(obj.orderitem_set.all(), many=True).data

    def get_total(self, obj):
        return obj.get_total()
