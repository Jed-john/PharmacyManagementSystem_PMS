from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from Pharmacy.forms import AddMedicineForm, AddSupplierForm
from Pharmacy.models import AddMedicine, AddSupplier
from accounts.decorators import pharmacist_required
from accounts.models import Pharmacist


# Create your views here.


# pharmacist dashboard views.
@login_required
@pharmacist_required
def pharmacist_dashboard(request):
    return render(request, 'pharmacypages/dashboard/pharmacist_dashboard.html')


# manage Medicines Views
@login_required
@pharmacist_required
def manage_medicine(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_medicines = AddMedicine.objects.filter(pharmacist=pharmacist_instance)
    return render(request, 'pharmacypages/manageMedicine/manageMedicine.html', {'all_medicines': all_medicines})

@login_required
@pharmacist_required
def add_medicine(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)

    if request.method == 'POST':
        form = AddMedicineForm(request.POST)
        if form.is_valid():
            medicine_instance = form.save(commit=False)
            medicine_instance.pharmacist = pharmacist_instance
            medicine_instance.save()

            # Redirect to the add_medicine_success view after successful form submission
            return redirect('add_medicine_success')
    else:
        form = AddMedicineForm()

    # Get all medicines for display
    all_medicines = AddMedicine.objects.filter(pharmacist=pharmacist_instance)

    return render(request, 'pharmacypages/manageMedicine/manageMedicine.html', {'form': form})


@login_required
@pharmacist_required
def add_medicine_success(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_medicines = AddMedicine.objects.filter(pharmacist=pharmacist_instance)
    # success message
    messages.success(request, 'Record Added Successfully')

    return render(request, 'pharmacypages/manageMedicine/add_medicine_success.html', {'all_medicines': all_medicines})


@login_required
@pharmacist_required
def edit_medicine(request, medicine_id):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    medicine = get_object_or_404(AddMedicine, id=medicine_id, pharmacist=pharmacist_instance)

    if request.method == 'POST':
        form = AddMedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            # Redirect to a success page or back to manage_medicine
            return redirect('manage_medicine')
    else:
        form = AddMedicineForm(instance=medicine)

    return render(request, 'pharmacypages/manageMedicine/edit_medicine.html', {'form': form, 'medicine': medicine})


@login_required
@pharmacist_required
def delete_medicine(request, medicine_id):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    medicine = get_object_or_404(AddMedicine, id=medicine_id, pharmacist=pharmacist_instance)

    if request.method == 'POST':
        # Handle form submission to delete the medicine
        medicine.delete()
        return redirect('manage_medicine')  # Redirect to the manage_medicine page

    return render(request, 'pharmacypages/manageMedicine/delete_medicine.html', {'medicine': medicine})


# pharmacist manage suppliers views
@login_required
@pharmacist_required
def manage_suppliers(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_suppliers = AddSupplier.objects.filter(pharmacist=pharmacist_instance)
    return render(request, 'pharmacypages/manageSuppliers/manageSuppliers.html', {'all_suppliers': all_suppliers})


@login_required
@pharmacist_required
def add_supplier(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)

    if request.method == 'POST':
        form = AddSupplierForm(request.POST, request.FILES)
        if form.is_valid():
            supplier_instance = form.save(commit=False)
            supplier_instance.pharmacist = pharmacist_instance
            supplier_instance.save()

            # Redirect to the manage_suppliers view after successful form submission
            return redirect('add_supplier_success')
    else:
        form = AddSupplierForm()

    # Get all suppliers for display
    all_suppliers = AddSupplier.objects.filter(pharmacist=pharmacist_instance)

    return render(request, 'pharmacypages/manageSuppliers/manageSuppliers.html', {'form': form, 'all_suppliers': all_suppliers})


@login_required
@pharmacist_required
def add_supplier_success(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_suppliers = AddSupplier.objects.filter(pharmacist=pharmacist_instance)
    # success message
    messages.success(request, 'Record Added Successfully')

    return render(request, 'pharmacypages/manageSuppliers/add_Supplier_success.html', {'all_suppliers': all_suppliers})

