from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import  Pharmacist, Customer
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class PharmacistSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmacist-input'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'pharmacist-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pharmacist-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pharmacist-input',
                                                                  'placeholder': 'Confirm Password'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmacist-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmacist-input'}))
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmacist-input'}))

    pharmacy_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmName-input'}))
    business_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'pharmacist-input'}))

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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input',
                                                                  'placeholder': 'Confirm Password'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))

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
