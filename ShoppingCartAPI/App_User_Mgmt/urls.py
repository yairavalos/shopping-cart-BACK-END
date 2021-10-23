# Standard Libraries and Packages

from django.contrib import admin
from django.urls import path, include

# Views
from .views import UsersIntroAPI, UserJobOrderList, UserJobOrderListCreate, UserShoppingCartList, UserShoppingCartListCreate

app_name = 'App_User_Mgmt'

# End-Points
urlpatterns = [
    path('', UsersIntroAPI.as_view()),
    path('purchase_order/', UserJobOrderList().as_view()), # GET Method
    path('purchase_order/generate_job/', UserJobOrderListCreate().as_view()), # POST Method
    path('shopping_cart/', UserShoppingCartList().as_view()), # GET Method
    path('shopping_cart/generate_bom/', UserShoppingCartListCreate().as_view()), # POST Method
]
