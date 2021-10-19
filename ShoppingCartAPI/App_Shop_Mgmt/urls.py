# Standard Libraries and Packages

from django.contrib import admin
from django.urls import path, include

# Views
from .views import ShopIntroAPI

app_name = 'App_Shop_Mgmt'

# End-Points
urlpatterns = [
    path('', ShopIntroAPI.as_view()),
]
