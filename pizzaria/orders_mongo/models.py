from django.db import models

from products_mongo.models import ProductMongo

class OrderMongo(models.Model):
    Product = models.ManyToManyField(ProductMongo, related_name='orders')
    
    
    def __str__(self):
        return f' {self.Product.Name}'


    
    
    

