# Standard Libraries and Packages

from re import I
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from .models import ProductCatalog, ProductStock

# Serializers
from .serializers import ProductCatalogSerializer, ProductStockSerializer

# Create your views here.

class ShopIntroAPI(APIView):
    """
    Shop App Management API Welcome View
    """
    def get(self, request):
        return Response('This is Shop App Management Welcome View')


class ShopProductCatalogList(generics.ListAPIView):
    """
    This View Class purpose is to retrieve the full Product Catalog from Shop Model Storage    
    """

    queryset = ProductCatalog.objects.all()
    serializer_class = ProductCatalogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product_category','product_description','product_part_number']
    ordering_fields = ['product_category']


class ShopProductStockList(generics.ListAPIView):
    """
    This View Class purpose is to retrieve the current Stock at Warehouse
    """

    queryset = ProductStock.objects.filter(product_stock_qty__gt=0)
    serializer_class = ProductStockSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product__product_category','product__product_description','product__product_part_number']
    ordering_fields = ['product__product_category']
