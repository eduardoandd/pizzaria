from django.contrib import admin
from django.urls import path
from customers.views import CustomersCreateListView,CustomersRetrieveUpdateDestroyView
from orders_mongo.views import OrderMongoCreateListView,OrderMongoRetrieveUpdateDestroyView
from deliveries_mongo.views import DeliveryMongoCreateListView,DeliveryMongoRetrieveUpdateDestroyView
from products_mongo.views import ProductMongoCreateListView, ProductMongoRetrieveUpdateDestroyView
from sales.views import SalesView
from stock.views import StockCreateListView,StockRetrieveUpdateDestroyView

from employees.views import EmployeesCreateListView,EmployeesRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('customers/', CustomersCreateListView.as_view(), name = 'customers_create_list'),
    path('customers/<int:pk>', CustomersRetrieveUpdateDestroyView.as_view(), name = 'customers_detail_view'),
    
    path('products-mongo/', ProductMongoCreateListView.as_view(), name='product_mongo_create_list'),
    path('products-mongo/<int:pk>', ProductMongoRetrieveUpdateDestroyView.as_view(), name='product_mongo_detail_view'),
    
    path('orders-mongo/', OrderMongoCreateListView.as_view(), name = 'orders_mongo_create_list'),
    path('orders-mongo/<int:pk>', OrderMongoRetrieveUpdateDestroyView.as_view(), name = 'orders_mongo_detail_view'),
    
    path('delivery/', DeliveryMongoCreateListView.as_view(), name = 'delivery_create_list'),
    path('delivery/<int:pk>', DeliveryMongoRetrieveUpdateDestroyView.as_view(), name = 'delivery_detail_view'),
    
    path('stock/', StockCreateListView.as_view(), name = 'stock_create_list'),
    path('stock/<int:pk>', StockRetrieveUpdateDestroyView.as_view(), name = 'stock_detail_view'),
    
    path('employees/', EmployeesCreateListView.as_view(), name = 'employees_create_list'),
    path('employees/<int:pk>', EmployeesRetrieveUpdateDestroyView.as_view(), name = 'employees_detail_view'),
    
    path('sales/', SalesView.as_view(), name = 'sales_list'),
    
    
    
]
