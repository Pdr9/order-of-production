from django.db import models

# Create your models here.
class OrdemdeProducao(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)

    