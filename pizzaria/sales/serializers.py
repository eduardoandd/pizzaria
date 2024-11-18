from rest_framework import serializers
from orders_mongo.models import OrderMongo
from sales.models import SalesMongo

class SalesMongoSerializer(serializers.ModelSerializer):
    order_count = serializers.SerializerMethodField()

    class Meta:
        model = SalesMongo
        fields = '__all__'

    def get_order_count(self, obj):
        return OrderMongo.objects.count()  # Corrigido
