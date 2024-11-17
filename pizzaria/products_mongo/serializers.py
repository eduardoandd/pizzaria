from rest_framework import serializers
from products_mongo.models import ProductMongo

class ProductMongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMongo
        fields='__all__'
    