# Standard Libraries and Packages

from django.db import models

# Import System Models
from django.conf import global_settings
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT

# Import External Models
from App_Shop_Mgmt.models import ProductCatalog, ProductLogistics

# Create your models here.

class UserProfile(models.Model):
    """
    WARNING !!!

    We are using this model combined with system Auth User Table.
    This model complement some extra features to shape User Profile
    """
    GENDER_TYPE = (
        ('female','Female'),
        ('male','Male'),
        ('other','Other'),
    )

    user_profile = models.OneToOneField(to=global_settings.AUTH_USER_MODEL, on_delete=PROTECT, related_name='user_profiles')
    user_address = models.CharField(max_length=300)
    user_gender = models.CharField(choices=GENDER_TYPE, max_length=10)
    user_age = models.IntegerField()

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.user_profile} | gender: {self.user_gender} | age: {self.user_age}'


class UserJob(models.Model):
    """
    WARNING !!!

    We are using this model combined with system Auth User Table.
    We are using this model in order to track user purchase job orders from Shopping App
    """

    user_profile = models.ForeignKey(to=global_settings.AUTH_USER_MODEL, on_delete=PROTECT, related_name='user_jobs')
    user_job_status = models.ForeignKey(to=ProductLogistics, on_delete=PROTECT, related_name='user_logistics')
    user_job_purchase_date = models.DateField(auto_now_add=True)
    user_job_delivery_date = models.DateField()

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.user_profile} | job status: {self.user_job_status} | purchase date: {self.user_job_purchase_date} | delivery date: {self.user_job_delivery_date}'
        

class UserPurchase(models.Model):
    """
    We are using this model to track user´s job order's BOM (Bill Of Materials)
    """

    user_job_id = models.ForeignKey(to=UserJob, on_delete=CASCADE, related_name='user_jobs')
    shop_product_id = models.ForeignKey(to=ProductCatalog, on_delete=PROTECT, related_name='user_products')
    user_product_qty = models.IntegerField()

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'job id: {self.user_job_id} | product id: {self.shop_product_id} | product qty: {self.user_product_qty}'

