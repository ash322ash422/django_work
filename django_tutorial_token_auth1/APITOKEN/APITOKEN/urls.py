#from django.contrib import admin
from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    #In postman: use URL=http://127.0.0.1:8000/hello/ with method=GET, then select 'Headers' tab and
    #put key='Authorization' and value='Token 9a3faecbe7a754de5866d11eeeaf893f55aaa991'
    path('hello/', views.HelloView.as_view(), name='hello'),
    
    #1)To get the token for user, send a POST request with username and password. See test_core.py
    #2)You can also use POSTMAN:Enter URL=http://127.0.0.1:8000/api-token-auth/ with method=POST,
    # then select the 'Body' tab and under 'raw' enter {"username":"admin","password": "admin"}
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
