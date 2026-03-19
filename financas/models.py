from django.db import models

# Create your models here.

class Conta():
    valor = models.DecimalField(max_digits=2)
