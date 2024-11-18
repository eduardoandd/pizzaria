from decimal import Decimal
from django.db import models

from products_mongo.models import ProductMongo

class OrderMongo(models.Model):
    Product = models.ManyToManyField(ProductMongo, related_name='orders')
    
    def total_price(self):
        total = sum(Decimal(product.Price.to_decimal())for product in self.Product.all())
        return total
    
    
    def __str__(self):
        return f' {self.Product.Name}'


    
    
    

