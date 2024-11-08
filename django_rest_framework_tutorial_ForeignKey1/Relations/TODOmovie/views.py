from django.http import JsonResponse
from .models import Book
from .serializer import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def watch_list(request, format=None):
    
    if request.method == 'GET':
        books = Book.objects.all() #get all books
        serializer = BookSerializer(books, many=True)
        #return JsonResponse(serializer.data, safe=False) #works
        #return JsonResponse({"books":serializer.data}, safe=False) #works
        return Response(serializer.data) 
    
    if request.method == 'POST': 
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
 