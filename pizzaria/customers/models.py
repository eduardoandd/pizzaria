from django.db import models

class Customers(models.Model):
    CustomersId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Agee = models.IntegerField()
