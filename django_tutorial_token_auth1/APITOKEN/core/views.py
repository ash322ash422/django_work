from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        content = {'message': 'Hello, Token Auth World!'}
        return Response(content)