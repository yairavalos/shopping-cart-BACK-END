# Generated by Django 3.2.8 on 2021-10-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_User_Mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userjob',
            name='user_job_purchase_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
