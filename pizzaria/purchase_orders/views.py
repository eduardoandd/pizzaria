from django.shortcuts import render
from rest_framework import generics
from purchase_orders.models import PurchaseOrder
from purchase_orders.serializers import PurchaseOrderSerializer

class PurchaseOrderCreateListView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class PurchaseOrderUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
