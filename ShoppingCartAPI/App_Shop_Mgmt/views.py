# Standard Libraries and Packages

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ShopIntroAPI(APIView):
    """
    Shop App Management API Welcome View
    """
    def get(self, request):
        return Response('This is Shop App Management Welcome View')
