from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from Customer.forms import MedicalInformationForm
from Customer.models import CustomerMedicine, MedicalInformation
from Pharmacy.models import AddMedicine
from accounts.decorators import customer_required
from accounts.models import Pharmacist


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


def pharmacist_list(request):
    pharmacists = Pharmacist.objects.all()
    customer = request.user.customer
    chosen_pharmacist = customer.my_pharmacist
    return render(request, 'customerPages/pharmacist_list.html', {'pharmacists': pharmacists, 'customer': customer, 'chosen_pharmacist': chosen_pharmacist})


def add_my_pharmacist(request):
    if request.method == "POST":
        pharmacist_id = request.POST.get("pharmacist_id")
        pharmacist = get_object_or_404(Pharmacist, user_id=pharmacist_id)
        request.user.customer.my_pharmacist = pharmacist
        request.user.customer.save()
        return redirect('pharmacist_list')
    return render(request, 'customerPages/mypharmacist.html')


@login_required
@customer_required
def medical_information(request):
    customer = request.user.customer
    medical_info, created = MedicalInformation.objects.get_or_create(customer=customer)

    if request.method == 'POST':
        form = MedicalInformationForm(request.POST, instance=medical_info)
        if form.is_valid():
            form.save()
    else:
        form = MedicalInformationForm(instance=medical_info)

    return render(request, 'customerPages/medical_information.html', {'customer': customer, 'form': form})