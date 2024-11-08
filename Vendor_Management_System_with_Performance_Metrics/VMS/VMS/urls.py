
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token 

app_name = "VMS"
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # METHOD 1) To generate token for user=admin by using command, use 
    # 'python manage.py drf_create_token admin'. This token is valid for infinitely long time.
    # METHOD 2)To get the token for user using postman:Enter URL=http://127.0.0.1:8000/api-token-auth/ with method=POST,
    # then select the 'Body' tab and under 'raw' enter {"username":"admin","password": "admin"}
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    #step 1)GET-> In postman: use URL=http://127.0.0.1:8000/api/vendors/ with method=GET, then select 'Headers' tab and
    #put key='Authorization' and value='Token <generated_token_here>'. This would retrieve all vendors
    #NOTE: If you do NOT provide token, then you will get {"detail":"Authentication credentials were not provided."}
    #step 2)POST-> In postman: use URL=http://127.0.0.1:8000/api/vendors/ with method=POST, then select 'Headers' tab and
    #put key='Authorization' and value='Token <generated_token_here>'. Then select 'Body' tab and using 'raw' option
    # put {"name": "vendor99", "contact_details": "vendor99 contact details here", "address": "vendor1 address here", "vendor_code":"99" }
    #This would create the above vendor. In postman, use double quotes, not single quotes.
    path("api/vendors/", views.VendorListCreateView.as_view(), name="vendors_list"),#Handles GET, POST
    
    #1)GET->In postman: use URL=http://127.0.0.1:8000/api/vendors/<primary_key_of_vendor>/ with method=GET,
    # then select 'Headers' tab and put key='Authorization' and value='Token <generated_token_here>'.
    # This method GET would retrieve record for the PK vendor.
    # 2)PUT-> In postman: use URL=http://127.0.0.1:8000/api/vendors/<primary_key_of_vendor>/ with method=PUT,
    # then select 'Headers' tab and put key='Authorization' and value='Token <generated_token_here>'.
    # Then select 'Body' tab and using 'raw' option
    # put {"name": "vendor_updated", "contact_details": "vendor updated details here", "address": "vendor1 updated address here", "vendor_code":"99" }
    # This method PUT would update record for the PK vendor.
    # 3) DELETE-> In postman: use URL=http://127.0.0.1:8000/api/vendors/<primary_key_of_vendor>/ with method=DELETE,
    # then select 'Headers' tab and put key='Authorization' and value='Token <generated_token_here>'.
    # This method DELETE would delete record for the PK vendor.
    path("api/vendors/<int:pk>/",views.VendorRetrieveUpdateDestroyView.as_view(),
         name="vendor_detail"), #Handles GET,PUT and DELETE
    
    #Below urls can be checked same way as above.
    path("api/vendors/<int:pk>/performance/",views.VendorPerformanceView.as_view(),
         name="vendor_performance",), #handles GET request
    
    path('api/purchase_orders/', views.PurchaseOrderListCreateView.as_view(), 
        name="purchase_order_list"), #handles GET and POST
    
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(),
        name="purchase_order_detail",), #handles 'GET','PUT','DELETE'
    
    path("api/purchase_orders/<int:pk>/acknowledge/",
        views.PurchaseOrderAcknowledgeView.as_view(),
        name="purchase_order_acknowledge",
        ), #Handles PATCH
]

