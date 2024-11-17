from rest_framework import serializers
from orders_mongo.models import OrderMongo

class OrderMongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMongo
        fields='__all__'
    

    