# Generated by Django 3.2.8 on 2021-10-21 00:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop_Mgmt', '0006_auto_20211020_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincoming',
            name='product_incoming_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productstock',
            name='product_stock_status_date',
            field=models.DateField(auto_now=True),
        ),
    ]
