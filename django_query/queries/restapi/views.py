from django.shortcuts import render
from webapp.models import Query
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializer import QuerySerializer
from webapp.my_utils import dbg
from  django.views import View
import asyncio
from django.http import HttpResponse

# Create your views here.
class QueryView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return HttpResponse(
            "GET http://127.0.0.1:8000/restapi/query/list/ <br/> \
            POST http://127.0.0.1:8000/restapi/query/create/ <br/> \
            PUT http://127.0.0.1:8000/restapi/query/update/{pk} <br/> \
            DELETE http://127.0.0.1:8000/restapi/query/delete/{pk} <br/> \
            GET http://127.0.0.1:8000/restapi/query/get/{pk}    ")

class QueryListAPIView(ListAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = QuerySerializer
    
    def get_queryset(self):
        #title = self.request.query_params.get('title', None)
        
        queryset = Query.objects.all()
        return queryset

class QueryCreateAPIView(CreateAPIView):
    serializer_class = QuerySerializer

class QueryUpdateAPIView(UpdateAPIView):
    serializer_class = QuerySerializer
    
    def get_queryset(self):
        dbg("inside QueryUpdateAPIView.get_queryset()")
        queryset = Query.objects.all()
        return queryset
    
    def update(self, request, *args, **kwargs):#override
        dbg("inside QueryUpdateAPIView.update()")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {"status": "success",
                "message": "CONGRATS: Query successfully updated.",
                "code": "success_query",
                },
                status=status.HTTP_200_OK,
                )

        else:
            return Response(
                {"status": "ffailureee",
                "message": "EERRROR: Query not updated.",
                "code": "ffail_query",
                },
                
                )

class QueryDeleteAPIView(DestroyAPIView):
    serializer_class = QuerySerializer
    
    def get_queryset(self):
        dbg("inside QueryDestroyAPIView.get_queryset()")
        queryset = Query.objects.all()
        return queryset
    
    #override. Called on DELETE. This method does not even call serializer
    def delete(self, request, *args, **kwargs): 
        dbg("inside QueryDeleteAPIView.delete")
        instance = self.get_object()
        dbg("..instance=", instance )
        dbg("..request.data=",request.data)
        
        instance.delete() # or-> self.perform_destroy(instance)  
        
        return Response(
            {"status": "success",
            "message": "CONGRATS: Query successfully deleted.",
            "code": "success_query",
            },
            status=status.HTTP_204_NO_CONTENT,
            )
class QueryRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuerySerializer
    
    def get_queryset(self): #override
        dbg("inside QueryRetrieveAPIView.get_queryset()")
        queryset = Query.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs): #override
        dbg("inside QueryRetrieveAPIView.retrieve")
        instance = self.get_object()
        
        serializer = self.get_serializer(instance)
        
        return Response(serializer.data)