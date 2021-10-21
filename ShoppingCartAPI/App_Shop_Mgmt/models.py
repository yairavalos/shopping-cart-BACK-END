# Standard Libraries and Packages

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.

class ProductVendor(models.Model):
    """
    This model represent the AVL (Approved Vendor List)
    """
    vendor_company_name = models.CharField(unique=True, max_length=150)
    vendor_contact_name = models.CharField(max_length=50)
    vendor_contact_email = models.EmailField(unique=True, max_length=90)

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.vendor_company_name}'


class ProductCatalog(models.Model):
    """
    This model represent the catalog of products that Shopping Cart Application has
    """
    CATEGORY_TYPE = (
        ('safety','Safety'),
        ('instruments','Instrumentations'),
        ('control','Control'),
        ('comms','Communications'),
        ('drivers','Drivers'),
        ('robots','Robotics'),
    )
    
    product_category = models.CharField(choices=CATEGORY_TYPE, max_length=30)
    product_vendor = models.ForeignKey(to=ProductVendor, on_delete=CASCADE, related_name='product_vendors')
    product_part_number = models.CharField(unique=True, max_length=20)
    product_description = models.CharField(max_length=150)
    product_img_link = models.URLField(max_length=250)
    product_unit_price = models.FloatField()
    product_lt_weeks = models.IntegerField()

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.product_category} | vendor: {self.product_vendor} | part number: {self.product_part_number} | desc: {self.product_description} | price: ${self.product_unit_price} USD'


class ProductStock(models.Model):
    """
    This model represent the current Product Stock into Warehouse
    Its a log that works with deltas, the difference between Incomes minus Outcomes gives the stock
    This is just a very, very, simple way to represent a Kanban Supermarket more than a Warehouse
    """
        
    product = models.OneToOneField(to=ProductCatalog, on_delete=PROTECT)
    product_stock_qty = models.IntegerField()
    product_stock_status_date = models.DateField(auto_now=True)

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.product} | qty: {self.product_stock_qty} | date: {self.product_stock_status_date}'


class ProductIncoming(models.Model):
    """
    This model represent the log for product incoming that has been received to enter into warehouse
    This is necessary in order to calculate deltas between purchase - incoming = stock
    """
    product_incoming = models.ForeignKey(to=ProductCatalog, on_delete=PROTECT, related_name='product_incomes')
    product_incoming_qty = models.IntegerField()
    product_incoming_date = models.DateField(auto_now_add=True)

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'{self.product_incoming} | qty: {self.product_incoming_qty} | date: {self.product_incoming_date}'


class ProductLogistics(models.Model):
    """
    This model represent the supply chain main flow for a Customer´s Purchase Job Order,
    related with Job Order Status this model helps to track the product in the User´s Job Order.
    
    In someway represents the business internal operations, but very simple
    """
    # This option would be manually selected by the admin
    # This emulate every step of the purchase process iternally into the Company
    DEPT_TYPE = (
        ('account','Accountant'),
        ('sales','Sales'),
        ('warehouse','Warehouse'),
        ('quality','Quality'),
        ('logistics','Logistics'),
    )

    process_step = models.CharField(unique=True, max_length=30)
    process_desc = models.CharField(max_length=100)
    process_dept = models.CharField(choices=DEPT_TYPE, max_length=20)
    process_lt_week = models.FloatField()

    # Str function to have a readable object description
    def __str__(self) -> str:
        return f'step: {self.process_step} | dept: {self.process_dept} | std LT: {self.process_lt_week} weeks'
