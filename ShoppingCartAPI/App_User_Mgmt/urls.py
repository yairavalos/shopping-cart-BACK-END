# Standard Libraries and Packages

from django.contrib import admin
from django.urls import path, include

# Views
from .views import UsersIntroAPI, UserJobOrderListCreate, UserShoppingCartListCreate

app_name = 'App_User_Mgmt'

# End-Points
urlpatterns = [
    path('', UsersIntroAPI.as_view()),
    path('purchase_order/', UserJobOrderListCreate().as_view()),
    path('shopping_cart/', UserShoppingCartListCreate().as_view()),
]
