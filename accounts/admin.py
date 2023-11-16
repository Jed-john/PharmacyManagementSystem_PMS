from django.contrib import admin
from .models import Pharmacist, Customer, User
import accounts.models

# Register your models here.
admin.site.register(User)
admin.site.register(Pharmacist)
admin.site.register(Customer)
