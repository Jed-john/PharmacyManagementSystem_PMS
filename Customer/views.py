from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from Customer.forms import MedicalInformationForm
from Customer.models import CustomerMedicine, MedicalInformation
from Pharmacy.models import AddMedicine
from accounts.decorators import customer_required
from accounts.models import Pharmacist, User

from django_daraja.mpesa.core import MpesaClient


# Create your views here.
@login_required
@customer_required
def customer_view_medicines(request):
    all_medicines = AddMedicine.objects.all()
    customer_medicines = CustomerMedicine.objects.filter(customer=request.user.customer)

    context = {
        'all_medicines': all_medicines,
        'customer_medicines': customer_medicines,
    }

    return render(request, 'customerPages/view_medicines.html', context)


# display registered pharmacists to customer
def pharmacist_list(request):
    pharmacists = Pharmacist.objects.all()
    customer = request.user.customer
    chosen_pharmacist = customer.my_pharmacist
    return render(request, 'customerPages/pharmacist_list.html', {'pharmacists': pharmacists, 'customer': customer, 'chosen_pharmacist': chosen_pharmacist})


# customer add pharmacist
def add_my_pharmacist(request):
    if request.method == "POST":
        pharmacist_id = request.POST.get("pharmacist_id")
        pharmacist = get_object_or_404(Pharmacist, user_id=pharmacist_id)
        request.user.customer.my_pharmacist = pharmacist
        request.user.customer.save()
        return redirect('pharmacist_list')
    return render(request, 'customerPages/pharmacist_list.html')


# Allow customer to change the pharmacist they chose
def remove_my_pharmacist(request):
    if request.method == "POST":
        request.user.customer.my_pharmacist = None
        request.user.customer.save()
    return redirect('pharmacist_list')


# customer medical info
@login_required
@customer_required
def medical_information(request):
    customer = request.user.customer
    medical_info, created = MedicalInformation.objects.get_or_create(customer=customer)

    if request.method == 'POST':
        form = MedicalInformationForm(request.POST, instance=medical_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical information saved successfully.')
            return redirect('display_medical_information')
    else:
        form = MedicalInformationForm(instance=medical_info)

    return render(request, 'customerPages/medical_information.html', {'customer': customer, 'form': form})


# customer payment views...one to display page, another to process
def makepayment(request):
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        quantity = int(request.POST.get('quantity', 0))
        phone_number = request.POST.get('phone_number')

        # Retrieve medicine or return a 404 response if not found
        medicine = get_object_or_404(AddMedicine, id=medicine_id)

        # Calculate total amount
        total_amount = int(medicine.pricePerUnitVolume) * quantity  # Convert to integer

        # Mpesa Daraja integration
        service = MpesaClient()
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'

        response = service.stk_push(phone_number, total_amount, account_reference, transaction_desc, callback_url)

        # Display success message and details
        messages.success(request, 'Payment initiated successfully. A pharmacist will get in touch with you '
                                  'after you complete payment.')

        return render(request, 'customerPages/makePayment.html', {'medicine': medicine, 'quantity': quantity, 'total_amount': total_amount})

    return render(request, 'customerPages/makePayment.html')