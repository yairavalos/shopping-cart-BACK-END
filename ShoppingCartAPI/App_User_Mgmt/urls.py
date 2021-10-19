# Standard Libraries and Packages

from django.contrib import admin
from django.urls import path, include

# Views
from .views import UsersIntroAPI

app_name = 'App_User_Mgmt'

# End-Points
urlpatterns = [
    path('', UsersIntroAPI.as_view()),
]
