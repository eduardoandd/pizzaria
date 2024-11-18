from rest_framework import serializers
from stock.models import StockMongo

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMongo
        fields='__all__'