
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_data(request):
    data = {"message": "Hello from Django!"}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_data(request):
    """- I sent raw data {"message": "Hello from React!"} using Postman in JSON format.
    """
    received_data = request.data
    # Here you can process the data
    print("Received POST data: ", received_data)
    response_data = {"message": "Data received successfully", "data": received_data}
    return Response(response_data, status=status.HTTP_201_CREATED)
