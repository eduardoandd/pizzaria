from django.db import models

class StockMongo(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()