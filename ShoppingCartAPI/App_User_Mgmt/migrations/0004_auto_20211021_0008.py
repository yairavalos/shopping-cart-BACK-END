# Generated by Django 3.2.8 on 2021-10-21 00:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_User_Mgmt', '0003_auto_20211020_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='userjob',
            name='user_job_delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 21, 0, 8, 13, 800055, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userjob',
            name='user_job_purchase_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
