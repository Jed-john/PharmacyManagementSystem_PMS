from django import forms

from Customer.models import MedicalInformation


class MedicalInformationForm(forms.ModelForm):
    class Meta:
        model = MedicalInformation
        fields = ['height', 'weight', 'age', 'gender', 'bmi', 'allergies', 'personal_diagnosis', 'family_diagnosis']
