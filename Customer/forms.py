from django import forms

from Customer.models import MedicalInformation


class MedicalInformationForm(forms.ModelForm):
    class Meta:
        model = MedicalInformation
        fields = ['height', 'weight', 'age', 'gender', 'bmi', 'allergies', 'personal_diagnosis', 'family_diagnosis', 'write_message_to_pharmacist' ]

    def save(self, commit=True):
        instance = super(MedicalInformationForm, self).save(commit=False)

        # Calculate BMI before saving the instance
        if instance.weight and instance.height:
            instance.bmi = round((instance.weight / (instance.height / 100) ** 2), 2)

        if commit:
            instance.save()

        return instance
