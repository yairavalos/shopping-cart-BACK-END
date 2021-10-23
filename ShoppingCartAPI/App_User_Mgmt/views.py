# Standard Libraries and Packages

from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from .models import UserProfile, UserJob, UserPurchase

# Serializers
from .serializers import UserJobSerializer, UserPurchaseSerializer

# Create your views here.

class UsersIntroAPI(APIView):
    """
    Users App Management API Welcome View
    """
    def get(self, request):
        return Response("This is User App Management Welcome View")


class UserJobOrderList(generics.ListAPIView):
    """
    This View Class purpose is to retrieve the list of job orders for product purcharse and delivery
    """

    queryset = UserJob.objects.all()
    serializer_class = UserJobSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id','=user_profile__username']
    ordering_fields = ['user_profile','user_job_purchase_date']


class UserShoppingCartList(generics.ListAPIView):
    """
    This View Class purpose is to retrieve the BOM (Bill of Materials) from a PO (Purchase Order)
    """

    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user_job__user_profile__id']
