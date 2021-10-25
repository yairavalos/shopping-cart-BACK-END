# Standard Libraries and Packages

from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from .models import UserProfile, UserJob, UserPurchase

# Serializers
from .serializers import UserJobSerializer, UserJobCreateSerializer, UserPurchaseSerializer, UserPurchaseCreateSerializer

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
    ordering_fields = ['id','user_profile','user_job_purchase_date']


class UserJobOrderListCreate(generics.ListCreateAPIView):
    """
    This View Class purpose is to retrieve the list of job orders for product purcharse and delivery
    """

    queryset = UserJob.objects.all()
    serializer_class = UserJobCreateSerializer
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


class UserShoppingCartListCreate(generics.ListCreateAPIView):
    """
    This View Class purpose is to retrieve the BOM (Bill of Materials) from a PO (Purchase Order)
    """

    queryset = UserPurchase.objects.all()
    serializer_class = UserPurchaseCreateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user_job__user_profile__id']

    def post(self, request):
        data = request.data

        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
