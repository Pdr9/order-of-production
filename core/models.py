from django.db import models
from datetime import date

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)
    data = models.DateField(default=date.today)