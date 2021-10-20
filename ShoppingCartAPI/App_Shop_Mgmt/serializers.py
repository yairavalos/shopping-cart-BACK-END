# Standard Libraries and Packages
from rest_framework import serializers

# Models
from .models import ProductCatalog, ProductStock

# Create Serializers
class ProductCatalogSerializer(serializers.ModelSerializer):
    """
    This serializer helps as interface for Product Catalog Model
    """

    class Meta:
        model = ProductCatalog
        fields = ['id','product_category', 'product_vendor','product_part_number','product_description','product_img_link','product_unit_price','product_lt_weeks']


class ProductStockSerializer(serializers.ModelSerializer):
    """
    This serializer helps as interface for Product Stock Model
    """

    class Meta:
        model = ProductStock
        fields = ['id','product','product_stock_qty','product_stock_status','product_stock_status_date']

