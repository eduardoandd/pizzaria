from rest_framework import serializers

from employees.models import EmployeesMongo


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesMongo
        fields= '__all__'