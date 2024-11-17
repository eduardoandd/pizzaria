from rest_framework import serializers
from purchase_orders.models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    totalPrice = serializers.SerializerMethodField()
    class Meta:
        model = PurchaseOrder
        fields='__all__'
    
    def get_totalPrice(self, obj):
        return obj.totalPrice()
    