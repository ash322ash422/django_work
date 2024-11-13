# myapp/views_data.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Z1DataView(APIView):
    def post(self, request):
        # Extract the 'number' from the request data
        user_number = request.data.get("number", None)
        if user_number is None:
            return Response({"error": "Number not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate or fetch the z1 data based on the input number
        z1_data = self.generate_z1_data(int(user_number))
        
        # Return the data as JSON
        return Response({"z1": z1_data, "number": user_number}, status=status.HTTP_200_OK)

    def generate_z1_data(self, user_number):
        # Example function to create a 2D list of z1 data based on user_number
        # Replace this with actual logic to retrieve or generate the data as needed
        size = 10  # Example size of z1_data grid
        z1_data = [[user_number + i + j for j in range(size)] for i in range(size)]
        return z1_data
