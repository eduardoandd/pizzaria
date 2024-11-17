from django.db import models

class ProductMongo(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.Name} - ${self.Price}'
    
    
