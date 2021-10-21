# Generated by Django 3.2.8 on 2021-10-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop_Mgmt', '0004_auto_20211020_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcatalog',
            name='product_category',
            field=models.CharField(choices=[('safety', 'Safety'), ('instruments', 'Instrumentations'), ('control', 'Control'), ('comms', 'Communications'), ('drivers', 'Drivers'), ('robots', 'Robotics')], max_length=30),
        ),
        migrations.AlterField(
            model_name='productincoming',
            name='product_incoming_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productstock',
            name='product_stock_status_date',
            field=models.DateField(auto_now=True),
        ),
    ]
