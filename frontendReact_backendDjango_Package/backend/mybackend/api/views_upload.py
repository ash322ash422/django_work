from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
import os
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("...Processing POST request from web client ")
        file = request.FILES.get('file')
        # print(".....file.name=",file.name)
        
        if not file:
            return Response({"message": "No file found in request"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the file in binary mode
        file_path = os.path.join(settings.DATA_DIR,'Well_1' ,file.name)
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        return Response({"message": f"File {file.name} uploaded successfully"}, status=status.HTTP_200_OK)

