from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from django.http import FileResponse
from rest_framework import status
import os
from rest_framework.parsers import MultiPartParser, FormParser

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("...Processing POST request from web client ")
        file = request.FILES.get('file')
        # print(".....file.name=",file.name)
        
        if not file:
            return Response({"message": "No file found in request"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the file in binary mode
        file_path = os.path.join("uploaded_files", file.name)
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        return Response({"message": f"File {file.name} uploaded successfully"}, status=status.HTTP_200_OK)

class FileDownloadView(APIView):
    def get(self, request, filename, *args, **kwargs):
        print("...Processing GET request from web client ")
        
        # Define the file path for download
        file_path = os.path.join("uploaded_files", filename) #This is directory where it is searching for file 
        if not os.path.exists(file_path):
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

        # Return the file as a response
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
