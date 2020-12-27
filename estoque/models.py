from django.db import models
from datetime import datetime  


class codigo_produto(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class medida(models.Model):
    codigo_produto = models.ForeignKey(codigo_produto, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Produto(models.Model):
    quantidade = models.DecimalField(default=1, max_digits=5, decimal_places=0)
    validade = models.DateField(null=True, blank=True)
    data_de_entrega = models.DateField(null=True, blank=True)
    codigo_produto = models.ForeignKey(codigo_produto, on_delete=models.SET_NULL, null=True)
    medida = models.ForeignKey(medida, on_delete=models.SET_NULL, null=True)