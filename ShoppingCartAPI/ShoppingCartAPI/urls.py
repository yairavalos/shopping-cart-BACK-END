"""ShoppingCartAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Standard Libraries and Packages

from django.contrib import admin
from django.urls import path, include

# Views
from .views import IntroAPI, UserIDCreateView, UserIDAuthTokenView

# End-Points
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', IntroAPI.as_view()),
    path('api/signup/', UserIDCreateView.as_view()),
    path('api/login/', UserIDAuthTokenView.as_view()),
    path('api/users/', include('App_User_Mgmt.urls')),
    path('api/shop/', include('App_Shop_Mgmt.urls')),
]
