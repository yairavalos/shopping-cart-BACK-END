# Generated by Django 3.2.8 on 2021-10-20 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('safety', 'Safety'), ('instruments', 'Instrumentations'), ('control', 'Control'), ('comss', 'Communications'), ('drivers', 'Drivers'), ('robots', 'Robotics')], max_length=30)),
                ('product_part_number', models.CharField(max_length=20, unique=True)),
                ('product_description', models.CharField(max_length=150)),
                ('product_img_link', models.URLField(max_length=250)),
                ('product_unit_price', models.FloatField()),
                ('product_lt_weeks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductLogistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_step', models.CharField(max_length=30, unique=True)),
                ('process_desc', models.CharField(max_length=100)),
                ('process_dept', models.CharField(max_length=30, unique=True)),
                ('process_lt_week', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_company_name', models.CharField(max_length=150, unique=True)),
                ('vendor_contact_name', models.CharField(max_length=50)),
                ('vendor_contact_email', models.EmailField(max_length=90, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_stock_qty', models.IntegerField()),
                ('product_stock_status', models.CharField(choices=[('income', 'INCOME'), ('outcome', 'OUTCOME')], max_length=10)),
                ('product_stock_status_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Shop_Mgmt.productcatalog')),
            ],
        ),
        migrations.AddField(
            model_name='productcatalog',
            name='product_vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_vendors', to='App_Shop_Mgmt.productvendor'),
        ),
    ]
