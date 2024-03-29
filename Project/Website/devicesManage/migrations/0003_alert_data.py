# Generated by Django 4.0.4 on 2022-07-05 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicesManage', '0002_rename_humidity_device_data_gas_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_id', models.CharField(max_length=30)),
                ('gas_value', models.IntegerField()),
                ('crnt_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
