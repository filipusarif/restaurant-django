from django.contrib import admin
from .models import  User, OwnerManager, Owner, CustomerManager, Customer

admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Customer)