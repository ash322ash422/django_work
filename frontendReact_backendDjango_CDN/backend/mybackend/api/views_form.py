from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import pandas as pd
import json

def process_df(df):
    # Example processing function (customize as needed)
    return df

@csrf_exempt  # Disable CSRF for this endpoint (useful for testing)
def submit_form(request):
    if request.method == 'POST':
        # Parse the JSON body of the request
        try:
            data = json.loads(request.body)
            print("Received data:", data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Define the path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'uploaded_files', 'z1_data.csv')  # Adjust path as needed
        
        # Attempt to load and process the CSV file
        try:
            df = pd.read_csv(csv_file_path)
            df = process_df(df)
            z1_data = df.values.tolist()  # Convert DataFrame to list format
        except FileNotFoundError:
            return JsonResponse({"error": "CSV file not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

        # Append processed data to the response
        response_data = {
            "input_data": data,
            "z1": z1_data
        }
        
        # Send JSON response with both input and processed data
        return JsonResponse(response_data, status=200)

    # Return an error response if not a POST request
    return JsonResponse({'error': 'POST request required'}, status=405)
