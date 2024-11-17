from rest_framework import serializers
from orders_mongo.models import OrderMongo

class OrderMongoSerializer(serializers.ModelSerializer):
    totalprice = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderMongo
        fields='__all__'
    

    