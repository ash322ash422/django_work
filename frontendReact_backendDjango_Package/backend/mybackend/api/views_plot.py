from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
import os, json, subprocess, sqlite3
import pandas as pd
from pathlib import Path
from django.conf import settings
import plotly.graph_objects as go

POC_CODE_DIR = os.path.join(settings.BASE_DIR,'Code_for_POC','src')
PYTHON_VIRTUAL_PATH = os.path.join(settings.BASE_DIR.parent,'.venv','Scripts','python.exe')
# print("PYTHON_VIRTUAL_PATH=",PYTHON_VIRTUAL_PATH)

def _read_csv(csv_file_path):
    # Attempt to load and process the CSV file
    try:
        df_csv = pd.read_csv(csv_file_path)
        # df = process_df(df_csv)
        # z1_data = df.values.tolist()  # Convert DataFrame to list format
    except FileNotFoundError:
        return Response({"error": "CSV file not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return df_csv
    
def _execute_script():
    #execute the python shell script that directs the output to DB
    try:
        result = subprocess.run(
            [PYTHON_VIRTUAL_PATH,
             'Code_for_POC/src/main.py'],  # Command to run the script
            capture_output=True,          # Capture standard output and error
            text=True                     # Return output as string
        )
        print("result.returncode=",result.returncode)
        # Check if the script executed successfully
        if result.returncode == 0:
            # return JsonResponse({"status": "success", "output": result.stdout})
            print("result.stdout=",result.stdout)
        else:
            # return JsonResponse({"status": "error", "output": result.stderr}, status=500)
            print("result.stderr=",result.stderr)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500) #TODO make it Response

def _read_db():
    conn = sqlite3.connect("example.db")
    df_from_db = pd.read_sql("SELECT * FROM series_table", conn)
    conn.close()
    return df_from_db    


def _process_df(df_csv, df_from_db):
    return df_csv
    # return df_from_db 
    
    
@api_view(['POST'])
def plot(request):
    print("..inside plot")
    # Only process POST requests
    if request.method == 'POST':
        # Access and validate JSON data in the request
        try:
            data = request.data  # Django REST Framework automatically parses JSON to a dict
            print("Received data:", data)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
        
        csv_file_path = os.path.join(settings.DATA_DIR, 'Well_1', 'z1_data.csv')  #TODO Adjust path as needed
        df_csv = _read_csv(csv_file_path)
        _execute_script()
        df_from_db = _read_db()
        df = _process_df(df_csv, df_from_db)
        z1_data = df.values.tolist()  # Convert DataFrame to list format
        
        # Prepare response data
        response_data = {
            "input_data": data,
            "z1": z1_data
        }

        return Response(response_data, status=status.HTTP_200_OK)

    # Return error response if request method is not POST
    return Response({'error': 'POST request required'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def get_plot_data(request):
    print("..inside get_plot_data")
    
    if request.method == 'POST':
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Fetch the JSON data from the PlotlyFigure table
        cursor.execute("SELECT figure_json FROM PlotlyFigure ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        print("..inside 106")
        # If data is found, return it; otherwise, return an error message
        if result:
            figure_json = result[0]
            # Convert JSON string to dictionary for JsonResponse
            figure_data = json.loads(figure_json)
            print("..inside 112")
            return JsonResponse(figure_data)
        else:
            return JsonResponse({'error': 'No figure data found in the database'}, status=404)
        
    # Return error response if request method is not POST
    return JsonResponse({'error': 'POST request required'}, status=405)





