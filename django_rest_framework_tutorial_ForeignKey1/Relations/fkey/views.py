from django.http import JsonResponse
from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST']) 
def author_list(request, format=None):
    
    if request.method == 'GET': # Works
        authors = Author.objects.all() #get all 
        serializer = AuthorSerializer(authors, many=True)
        #return JsonResponse(serializer.data, safe=False) #works
        #return JsonResponse({"books":serializer.data}, safe=False) #works
        return Response(serializer.data) 
    
    if request.method == 'POST': # Creating a new record
        print("in POST")
        serializer = AuthorSerializer(data = request.data)
        print("serializer=",serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET','PUT','DELETE'])# PUT for updating data, DELETE for deleting the data. Works
def author_detail(request, id, format=None ):
    try:
      author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/author/2
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    elif request.method == 'PUT': #update
        serializer = AuthorSerializer(author, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        author.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
#end def
###########################################################


@api_view(['GET','POST']) #Works
def book_list(request, format=None):
    
    if request.method == 'GET':
        books = Book.objects.all() #get all 
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
            
@api_view(['GET','PUT','DELETE'])# PUT for updating data, DELETE for deleting the data. Works
def book_detail(request, id, format=None ):
    try:
      book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/books/2
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
#end class
