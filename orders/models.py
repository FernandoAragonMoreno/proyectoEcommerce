from django.db import models

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
    idCity = models.IntegerField()
    nameCity = models.CharField(max_length=255)
    descriptionCity = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photo", null=True, blank=True)
    assetCity = models.BooleanField()

class City_Customer(models.Model):
    idCity = models.IntegerField()
    idCustomer = models.IntegerField()

class Customer(models.Model):
    idCustomer = models.IntegerField()
    nameCustomer = models.CharField(max_length=255)
    assetCustomer = models.BooleanField()

class PaymentMethods(models.Model):
    idPaymentMethods = models.IntegerField()
    namePaymentMethods = models.CharField(max_length=255)
    assetPaymentMethods = models.BooleanField()

class PaymentMethods_Customer(models.Model):
    idPaymentMethods = models.IntegerField()
    idCustomer = models.IntegerField()

class Role(models.Model):
    idRole = models.IntegerField()
    nameRole = models.CharField(max_length=255)
    assetRole = models.BooleanField()

class Seller(models.Model):
    idSeller = models.IntegerField()
    nameSeller = models.CharField(max_length=255)
    assetSeller = models.BooleanField()