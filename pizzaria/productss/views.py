from django.shortcuts import render
from rest_framework import generics
from productss.models import Product
from productss.serializers import ProductSerializer

class ProductsCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
