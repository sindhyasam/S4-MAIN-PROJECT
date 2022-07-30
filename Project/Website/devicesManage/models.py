from django.db import models
from datetime import datetime

class Devices_list(models.Model):
    mac_id = models.CharField(max_length=30)
    assigned_to = models.CharField(max_length=30)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=5)


class Device_data(models.Model):
    mac_id = models.CharField(max_length=30)
    gas_value=models.IntegerField()
    crnt_time = models.DateTimeField(default=datetime.now, blank=True)


class Alert_data(models.Model):
    mac_id = models.CharField(max_length=30)
    gas_value=models.IntegerField()
    crnt_time = models.DateTimeField(default=datetime.now, blank=True)