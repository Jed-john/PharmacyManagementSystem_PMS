from django.contrib.auth.decorators import login_required
from django.db import models

from Pharmacy.models import AddMedicine
from accounts.models import Customer, User, Pharmacist


# Create your models here.

class CustomerMedicine(models.Model):
    medicine = models.ForeignKey(AddMedicine, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacist_medicines')
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.medicine.pricePerUnitVolume


class MedicalInformation(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True, related_name='medical_information')

    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)

    FAMILY_DIAGNOSIS_CHOICES = [
        ('TB', 'Tuberculosis'),
        ('DIABETES', 'Diabetes'),
        ('STROKE', 'Stroke'),
        ('HEART-DISEASE', 'Heart-Disease'),
        ('CANCER', 'Cancer'),
        ('OBESITY', 'Obesity'),
        ('ANAEMIA', 'Anaemia'),
        ('ASTHMA', 'Asthma'),
        ('THYROID-DISORDERS', 'Thyroid-Disorders'),
        ('NONE', 'None'),
        ('I DON"T KNOW', 'I don"t know')

    ]
    personal_diagnosis = models.CharField(max_length=20, choices=FAMILY_DIAGNOSIS_CHOICES, null=True, blank=True)
    family_diagnosis = models.CharField(max_length=20, choices=FAMILY_DIAGNOSIS_CHOICES, null=True, blank=True)

    write_message_to_pharmacist = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Medical Information for {self.customer.first_name} {self.customer.last_name}"

