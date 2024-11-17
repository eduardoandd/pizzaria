from django.shortcuts import render
from rest_framework import generics
from products_mongo.models import ProductMongo
from products_mongo.serializers import ProductMongoSerializer

class ProductMongoCreateListView(generics.ListCreateAPIView):
    queryset = ProductMongo.objects.all()
    serializer_class=ProductMongoSerializer

class ProductMongoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =ProductMongo.objects.all()
    serializer_class=ProductMongoSerializer
