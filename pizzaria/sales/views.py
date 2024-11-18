from rest_framework.generics import ListCreateAPIView
from sales.models import SalesMongo
from sales.serializers import SalesMongoSerializer

class SalesView(ListCreateAPIView):
    queryset = SalesMongo.objects.all()
    serializer_class = SalesMongoSerializer
