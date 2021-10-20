# Standard Libraries and Packages
from django.contrib import admin

# Models
from .models import UserProfile, UserJob, UserPurchase

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserJob)
admin.site.register(UserPurchase)
