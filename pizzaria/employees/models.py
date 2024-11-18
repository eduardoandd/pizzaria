from django.db import models

class EmployeesMongo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    