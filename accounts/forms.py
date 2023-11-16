from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import  Pharmacist, Customer
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class PharmacistSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    telephone_number = forms.CharField(widget=forms.TextInput())

    pharmacy_name = forms.CharField(widget=forms.TextInput())
    business_number = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pharmacist = True
        if commit:
            user.save()
        pharmacist = Pharmacist.objects.create(user=user, first_name=self.cleaned_data.get('first_name'),
                                            last_name=self.cleaned_data.get('last_name'),
                                            telephone_number=self.cleaned_data.get('telephone_number'),
                                            pharmacy_name=self.cleaned_data.get('pharmacy_name')),

        return user


class CustomerSignUpForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input',
                                                                  'placeholder': 'Confirm Password'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Last Name'}))
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input',
                                                                     'placeholder': 'Telephone Number'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        customer = Customer.objects.create(user=user, first_name=self.cleaned_data.get('first_name'),
                                          last_name=self.cleaned_data.get('last_name'),
                                          telephone_number=self.cleaned_data.get('telephone_number'))
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
