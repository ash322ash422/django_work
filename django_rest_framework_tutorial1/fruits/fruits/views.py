from django.http import JsonResponse
from  .models import Fruit
from  .serializer import FruitSerializer
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework import status

@api_view(['GET','POST'])
def fruit_list(request, format=None):
    
    if request.method == 'GET':
        fruits = Fruit.objects.all() #get all fruits
        serializer = FruitSerializer(fruits, many=True)
        #return JsonResponse(serializer.data, safe=False) #works
        #return JsonResponse({"fruits":serializer.data}, safe=False) #works
        return Response(serializer.data) 
    
    #If data= {"name": "Strawberry", "description": "Love it anytime"} is sent through POST method, say using postman app.,
    # then this data is saved and echoed back to the client. 
    if request.method == 'POST': 
        serializer = FruitSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
 
@api_view(['GET','PUT','DELETE'])# PUT for updating data, DELETE for deleting the data
def fruit_detail(request, id, format=None ):
    try:
      fruit = Fruit.objects.get(pk=id)
    except Fruit.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/fruits/2
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FruitSerializer(fruit, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        fruit.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)