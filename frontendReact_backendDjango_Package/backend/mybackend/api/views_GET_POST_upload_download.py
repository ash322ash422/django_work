from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json, os

# Handle GET requests to retrieve data
@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        # Example data to return (replace with your data source as needed)
        data = {
            "message": "Data fetched successfully",
            "x": [1, 2, 3, 4, 5],  # Example x-axis data
            "y": [10, 20, 15, 25, 30]  # Example y-axis data
        }
        return JsonResponse(data, safe=False)

# Handle POST requests to receive and process data
@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get("message", "")
            # Process the message or perform any action
            response_data = {
                "message": f"Data received successfully: {message}"
            }
            return JsonResponse(response_data, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

# Handle file upload via POST
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return JsonResponse({"message": f"File uploaded successfully: {filename}", "file_url": file_url})

    return JsonResponse({"error": "No file uploaded"}, status=400)

# Handle file download by filename
@csrf_exempt
def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    return JsonResponse({"error": "File not found"}, status=404)
