from django.db import models

class OrderMongo(models.Model):
    Product = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f'R${self.Price} - {self.Product}'


    
    
    

