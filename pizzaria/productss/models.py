from django.db import models

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)