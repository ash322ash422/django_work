from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from django.conf import settings
import os

class Z1DataView(APIView):
    def post(self, request):
        print("...received POST request")
        number = request.data.get('number')
        # Example z1 data (previous data)
        csv_file_path = os.path.join(settings.BASE_DIR, 'uploaded_files/z1_data.csv')  # Modify path as needed
        
        # Load the CSV file data using pandas
        try:
            df = pd.read_csv(csv_file_path)
            print("df=",df)
            z1_data = df.values.tolist()  # Convert DataFrame to list format
        except FileNotFoundError:
            return Response({"error": "CSV file not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        return Response({"number": number, "z1": z1_data})
    
    
    