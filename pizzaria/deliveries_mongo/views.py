from django.shortcuts import render
from rest_framework import generics
from deliveries_mongo.models import DeliveryMongo
from deliveries_mongo.serializers import DeliveryMongoSerializer

class DeliveryMongoCreateListView(generics.ListCreateAPIView):
    queryset = DeliveryMongo.objects.all()
    serializer_class=DeliveryMongoSerializer

class DeliveryMongoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =DeliveryMongo.objects.all()
    serializer_class=DeliveryMongoSerializer
