# Standard Libraries and Packages
from django.db import models
from rest_framework import serializers

# Models
from .models import User, UserProfile, UserJob, UserPurchase

# External Models
from App_Shop_Mgmt.models import ProductStock, ProductLogistics

# External Serializers
from App_Shop_Mgmt.serializers import ProductLogisticSerializer

# Here create your Serializers

class UserIdSerializer(serializers.ModelSerializer):
    """
    This serializer help as interface to Model User Profile
    """

    class Meta:
        model = User
        fields = ['id','username'] # username


class UserJobSerializer(serializers.ModelSerializer):
    """
    This serializer helps as interface to Model UserJob
    """
    user_profile = UserIdSerializer()
    user_job_status = ProductLogisticSerializer()

    class Meta:
        model = UserJob
        fields = ['id','user_profile','user_job_status','user_job_purchase_date','user_job_delivery_date']
        depth = 1


class UserPurchaseSerializer(serializers.ModelSerializer):
    """
    This serializer helps as interface to Model UserPurchase
    """
    user_job = UserJobSerializer()

    class Meta:
        model = UserPurchase
        fields = ['id','user_job','user_product','user_product_qty']
        depth = 1
