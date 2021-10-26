# Standard Libraries and Packages
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your serializers

class UserCreateSerializer(serializers.ModelSerializer):
    """
    This serializer helps as interface for User Model
    """

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):

        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        
        return user

