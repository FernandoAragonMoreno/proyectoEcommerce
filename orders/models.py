from django.db import models

# Create your models here.
class Ejemplo(models.Model):
    idEjemplo = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)