from django.conf.urls import url
from customers.views import *

urlpatterns = [
    url('customers/',CustomersCreateListView.as_view(), name='customers_create_list'),
    url('customers/',CustomersRetrieveUpdateDestroyView.as_view(), name='detail')
   
]
