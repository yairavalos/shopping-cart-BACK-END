# Standard Libraries and Packages
from django.contrib import admin

# Models
from .models import ProductVendor, ProductCatalog, ProductStock, ProductLogistics

# Register your models here.

admin.site.register(ProductVendor)
admin.site.register(ProductCatalog)
admin.site.register(ProductStock)
admin.site.register(ProductLogistics)
