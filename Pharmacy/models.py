

from django.db import models
from django.utils import timezone

from accounts.models import Pharmacist


# Create your models here.
# medicine models.
class AddMedicine(models.Model):
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, default=None)
    medicine_name = models.TextField()
    description = models.TextField()
    unitVolume = models.CharField(max_length=50)
    pricePerUnitVolume = models.CharField(max_length=50)
    count = models.IntegerField()
    expiryDate = models.DateField()

    # field for storing image path or URL that is used in online store
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)


# Suppliers models
class AddSupplier(models.Model):
    class Category(models.TextChoices):
        ORGANIZATION = 'Organization', 'Organization'
        INDIVIDUAL = 'Individual', 'Individual'

    class PaymentMethod(models.TextChoices):
        CHEQUE = 'Cheque', 'Cheque'
        EFT = 'EFT', 'EFT'

    class Status(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        INACTIVE = 'Inactive', 'Inactive'

    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, default=None)

    supplier_legalName = models.CharField(max_length=100)
    supplier_TradeName = models.CharField(max_length=100)
    supplier_GSTReGNo = models.CharField(max_length=60)
    category = models.CharField(max_length=50, choices=Category.choices)

    contact_name = models.CharField(max_length=100)
    contact_PhoneNumber = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_address1 = models.CharField(max_length=50)

    settlement_currency = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices)

    contract_startDate = models.DateField()
    contract_EndDate = models.DateField()
    contract_Document = models.FileField()

    status = models.CharField(max_length=20, choices=Status.choices)
    created_at = models.DateTimeField(default=timezone.now)
