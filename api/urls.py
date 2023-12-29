from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path("vendors",views.create_vendor,name="vendors"),
    path("vendors/<int:vendor_id>/",views.list_vendor,name="vendors"),
    path("vendors/<int:vendor_id>/performance",views.list_vendor,name="vendors"),
    path("purchase_orders",views.create_purchase_order,name="purchase_orders"),
    path("purchase_orders/<int:vendor_id>/",views.list_purchase_orders,name="purchase_orders"),
    
    
]
