from django.db import models
from bson.objectid import ObjectId
from djongo import models
from productss.models import Product

class PurchaseOrder(models.Model):
    OrderId = models.AutoField(primary_key=True)
    Products = models.ArrayReferenceField(
        to=Product,
        on_delete=models.CASCADE
    )
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    
    
