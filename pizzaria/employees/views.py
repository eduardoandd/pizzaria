from employees.serializers import EmployeesSerializer
from employees.models import EmployeesMongo
from rest_framework import generics

class EmployeesCreateListView(generics.ListCreateAPIView):
    queryset= EmployeesMongo.objects.all()
    serializer_class = EmployeesSerializer
    
class EmployeesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeesMongo.objects.all()
    serializer_class = EmployeesSerializer

