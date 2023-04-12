from django.db import models
from datetime import datetime
from datetime import date

class Pessoa(models.Model):
    op = models.IntegerField(null=True)
    article = models.CharField(max_length=50, default="")
    data = models.DateField(default=date.today)
    nf_fornecida = models.IntegerField(default=0)
    nf_ret = models.IntegerField(default=0)
    nf_ind = models.IntegerField(default=0)
    total_received = models.IntegerField(default=0)
    first_quality = models.IntegerField(default=0)
    second_quality = models.IntegerField(default=0)
    third_quality = models.IntegerField(default=0)
    timemoney = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    value_pieces = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=12)
    date_shipment = models.DateField(default=date.today)
    approval_date = models.DateField(default=date.today)
    preview_payment = models.DateField(default=date.today)
    date_payment = models.DateField(default=date.today)