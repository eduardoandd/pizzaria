from django.db import models

from orders_mongo.models import OrderMongo

class DeliveryMongo(models.Model):
    # DeliveryId = models.CharField(max_length=20, unique=True)
    shipping = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.ForeignKey(OrderMongo, on_delete=models.CASCADE, related_name='deliveries')
    
    
