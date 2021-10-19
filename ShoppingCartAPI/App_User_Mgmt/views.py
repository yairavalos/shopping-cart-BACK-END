# Standard Libraries and Packages

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UsersIntroAPI(APIView):
    """
    Users App Management API Welcome View
    """
    def get(self, request):
        return Response("This is User App Management Welcome View")