# Standard Libraries and Packages

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Serializers
from .serializers import UserCreateSerializer

# Create your views here.

class IntroAPI(APIView):
    """
    Users App Management API Welcome View
    """
    def get(self, request):
        return Response("This is User App Management Welcome View")


class UserIDCreateView(generics.CreateAPIView):
    """
    This view its intended for User  Generation
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        user = User.objects.get(id=token.user_id)
        
        return Response({'id':token.user_id, 'username':user.username, 'token': token.key })


class UserIDAuthTokenView(ObtainAuthToken):
    """
    This view its intended to give a little more detail in order to 
    address users correctly into end-points filters
    """

    def post(self, request, *args, **kwargs):
        response =  super(UserIDAuthTokenView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({
            'id':token.user_id, 
            'user':user.username, 
            'token': token.key 
            })
