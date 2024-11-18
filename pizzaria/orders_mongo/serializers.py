from rest_framework import serializers
from orders_mongo.models import OrderMongo

class OrderMongoSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderMongo
        fields='__all__'
    
    def get_total_price(self, obj):
        return obj.total_price()

    