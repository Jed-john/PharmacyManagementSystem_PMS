from django import forms

from Pharmacy.models import AddMedicine, AddSupplier


class AddMedicineForm(forms.ModelForm):
    medicine_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'medicine-input'}))
    description = forms.CharField(widget=forms.Textarea())
    unitVolume = forms.CharField(widget=forms.TextInput(attrs={'class': 'medicine-input'}))
    pricePerUnitVolume = forms.CharField(widget=forms.TextInput(attrs={'class': 'medicine-input'}))
    count = forms.CharField(widget=forms.TextInput(attrs={'class': 'medicine-input'}))

    class Meta:
        model = AddMedicine
        fields = ('medicine_name', 'description', 'unitVolume', 'pricePerUnitVolume', 'count')


# Add supplier form
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = AddSupplier
        fields = ('supplier_legalName', 'supplier_TradeName', 'supplier_GSTReGNo', 'category', 'contact_name',
                  'contact_PhoneNumber', 'contact_email', 'contact_address1', 'settlement_currency', 'payment_method',
                  'contract_startDate', 'contract_EndDate', 'contract_Document', 'status')
        widgets = {
            'contract_startDate': forms.TextInput(attrs={'class': 'datepicker'}),
            'contract_EndDate': forms.TextInput(attrs={'class': 'datepicker'})
        }

    category = forms.ChoiceField(choices=AddSupplier.Category.choices, widget=forms.Select(attrs={'class': 'custom-supplier'}))
    payment_method = forms.ChoiceField(choices=AddSupplier.PaymentMethod.choices, widget=forms.Select(attrs={'class': 'custom-supplier'}))
    status = forms.ChoiceField(choices=AddSupplier.Status.choices, widget=forms.Select(attrs={'class': 'custom-supplier'}))

    supplier_legalName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'supplier-input'}))
    supplier_TradeName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'supplier-input'}))
    supplier_GSTReGNo = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'supplier-input'}))

    contact_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'supplier-input'}))
    contact_PhoneNumber = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'supplier-input'}))
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'supplier-input'}))
    contact_address1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'supplier-input'}))

    settlement_currency = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'supplier-input'}))

    contract_startDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker supplier-input'}))
    contract_EndDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker supplier-input'}))
    contract_Document = forms.FileField(widget=forms.FileInput(attrs={'class': 'supplier-input'}))

