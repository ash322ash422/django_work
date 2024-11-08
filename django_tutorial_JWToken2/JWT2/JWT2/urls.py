from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    #METHOD 1) Following URL page would prompt for an active user and password and retuns the token pair(access and refresh)
    #METHOD 2) To get the token for user using postman:Enter URL=http://127.0.0.1:8000/auth/token/ with method=POST,
    # then select the 'Body' tab and under 'raw' enter {"username":"admin","password": "admin"}
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), #returns access and refresh token
    
    #Following prompts for a refresh type JSON web token and returns an access type JSON web
    # token if the refresh token is valid
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path('', include('mainapp.urls')),
]