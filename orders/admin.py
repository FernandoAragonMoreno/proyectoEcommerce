from django.contrib import admin
from .models import Country, City, City_Customer, Customer, PaymentMethods, PaymentMethods_Customer, Role, Seller #Ejemplo, 

# Register your models here.
#admin.site.register(Ejemplo)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(City_Customer)
admin.site.register(Customer)
admin.site.register(PaymentMethods)
admin.site.register(PaymentMethods_Customer)
admin.site.register(Role)
admin.site.register(Seller)
#admin.site.register(User)