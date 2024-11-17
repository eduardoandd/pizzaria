from customers.models import Customers
from customers.serializers import CustomerSerializer
from rest_framework import generics



class CustomersCreateListView(generics.ListCreateAPIView):
    queryset= Customers.objects.all()
    serializer_class = CustomerSerializer
    
class CustomersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

