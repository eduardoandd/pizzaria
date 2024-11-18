from django.shortcuts import render
from stock.serializers import StockSerializer
from stock.models import StockMongo
from rest_framework import generics

class StockCreateListView(generics.ListCreateAPIView):
    queryset= StockMongo.objects.all()
    serializer_class = StockSerializer
    
class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockMongo.objects.all()
    serializer_class = StockSerializer

