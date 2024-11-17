from django.shortcuts import render
from rest_framework import generics
from orders_mongo.models import OrderMongo
from orders_mongo.serializers import OrderMongoSerializer

class OrderMongoCreateListView(generics.ListCreateAPIView):
    queryset = OrderMongo.objects.all()
    serializer_class=OrderMongoSerializer

class OrderMongoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =OrderMongo.objects.all()
    serializer_class=OrderMongoSerializer
