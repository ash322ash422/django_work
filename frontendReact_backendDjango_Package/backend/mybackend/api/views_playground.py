from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.http import JsonResponse
# from django.conf import settings

#This is for testing purposes
@api_view(['POST'])
def play_json_response(request):
    # Only process POST requests
    if request.method == 'POST':
        response_data = {
            "input_data": 'data',
            "z1": ['z1_data']
        }

        # Return JSON response with both input and processed data
        return Response(response_data, status=status.HTTP_200_OK)

    # Return error response if request method is not POST
    return Response({'error': 'POST request required'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



