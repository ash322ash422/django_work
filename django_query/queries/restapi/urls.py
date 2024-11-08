from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    # invoked on GET http://127.0.0.1:8000/restapi/query/
    path('query/', views.QueryView.as_view(), name='query_home'), #invoked on GET
    
    # invoked on GET http://127.0.0.1:8000/restapi/query/list/
    path('query/list/', views.QueryListAPIView.as_view(), name='api_query_list'), #invoked on GET
    
    # invoked on POST http://127.0.0.1:8000/restapi/query/create/
    path('query/create/', views.QueryCreateAPIView.as_view(), name='api_query_create'), 
    
    # invoked on PUT http://127.0.0.1:8000/restapi/query/update/<pk>
    path('query/update/<int:pk>', views.QueryUpdateAPIView.as_view(), name='api_query_update'), 
    
    # invoked on DELETE http://127.0.0.1:8000/restapi/query/delete/<pk>
    path('query/delete/<int:pk>', views.QueryDeleteAPIView.as_view(), name='api_query_delete'), 

    # invoked on GET http://127.0.0.1:8000/restapi/query/get/<pk>
    path('query/retrieve/<int:pk>', views.QueryRetrieveAPIView.as_view(), name='api_query_retrieve'), 
 
    
]