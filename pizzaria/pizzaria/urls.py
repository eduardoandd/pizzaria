from django.contrib import admin
from django.urls import path
from customers.views import CustomersCreateListView,CustomersRetrieveUpdateDestroyView
from productss.views import ProductsCreateListView,ProductsRetrieveUpdateDestroyView
from purchase_orders.views import PurchaseOrderCreateListView,PurchaseOrderRetrieveUpdateDestroyView
from orders_mongo.views import OrderMongoCreateListView,OrderMongoRetrieveUpdateDestroyView
from deliveries_mongo.views import DeliveryMongoCreateListView,DeliveryMongoRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('customers/', CustomersCreateListView.as_view(), name = 'customers_create_list'),
    path('customers/<int:pk>', CustomersRetrieveUpdateDestroyView.as_view(), name = 'customers_detail_view'),
    
    path('products/', ProductsCreateListView.as_view(), name = 'products_create_list'),
    path('products/<int:pk>', ProductsRetrieveUpdateDestroyView.as_view(), name = 'products_detail_view'),
    
    path('orders/', PurchaseOrderCreateListView.as_view(), name = 'orders_create_list'),
    path('orders/<int:pk>', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name = 'orders_detail_view'),
    
    path('orders-mongo/', OrderMongoCreateListView.as_view(), name = 'orders_mongo_create_list'),
    path('orders-mongo/<int:pk>', OrderMongoRetrieveUpdateDestroyView.as_view(), name = 'orders_mongo_detail_view'),
    
    path('delivery/', DeliveryMongoCreateListView.as_view(), name = 'delivery_create_list'),
    path('delivery/<int:pk>', DeliveryMongoRetrieveUpdateDestroyView.as_view(), name = 'delivery_detail_view'),
    
    
]
