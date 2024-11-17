from rest_framework import serializers
from deliveries_mongo.models import  DeliveryMongo

class DeliveryMongoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeliveryMongo
        fields='__all__'
