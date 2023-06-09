from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Ejemplo(models.Model):
#     idEjemplo = models.IntegerField()
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)


class Country(models.Model):
    idCountry = models.IntegerField()
    nameCountry = models.CharField(max_length=50)
    descriptionCountry = models.CharField(max_length=200)
    assetCountry = models.BooleanField()

class City(models.Model):
    idCountry = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    idCity = models.IntegerField()
    nameCity = models.CharField(max_length=50)
    descriptionCity = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photo")
    assetCity = models.BooleanField()

    def __str__(self):
        return self.nameCity

class City_Customer(models.Model):
    idCity = models.IntegerField()
    idCustomer = models.IntegerField()

class Customer(models.Model):
    idUser = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    idCustomer = models.IntegerField()
    nameCustomer = models.CharField(max_length=50)
    assetCustomer = models.BooleanField()

class PaymentMethods(models.Model):
    idPaymentMethods = models.IntegerField()
    namePaymentMethods = models.CharField(max_length=50)
    assetPaymentMethods = models.BooleanField()

class PaymentMethods_Customer(models.Model):
    idPaymentMethods = models.IntegerField()
    idCustomer = models.IntegerField()

class Role(models.Model):
    idUser = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    idRole = models.IntegerField()
    nameRole = models.CharField(max_length=50)
    assetRole = models.BooleanField()

class Seller(models.Model):
    idUser = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    idSeller = models.IntegerField()
    nameSeller = models.CharField(max_length=50)
    assetSeller = models.BooleanField()