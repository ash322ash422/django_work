from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class Home(APIView):
    authentication_classes = [JWTAuthentication]# Authentication identifies the user
    
    #Following determines if the user has permission to perform a specific action
    #(e.g.AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
    permission_classes = [IsAuthenticated]# Allows only authenticated users to access this view

    def get(self, request):
        content = {'message': 'Hello, JW Token World!'}
        return Response(content)