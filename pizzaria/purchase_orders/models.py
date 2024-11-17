from django.db import models

class PurchaseOrder(models.Model):
    OrderId = models.AutoField(primary_key=True)
    Products = models.JSONField()

    def totalPrice(self):
        """ Calcular o preço total dos produtos na lista. """
        
        if not isinstance(self.Products,list):
            return 0
        return sum(product.get('price',0) for product in self.Products)
    
    
