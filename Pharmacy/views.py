from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from Pharmacy.forms import AddMedicineForm, AddSupplierForm, ImageAssociationForm
from Pharmacy.models import AddMedicine, AddSupplier
from accounts.decorators import pharmacist_required
from accounts.models import Pharmacist, Customer


# Create your views here.


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

    return render(request, 'pharmacypages/manageMedicine/addmedicine.html', {'form': form})


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
            print("Medicine saved successfully!")  # for debugging
            return redirect('manageMedicine')
        else:
            print("Form is not valid!")  # for debugging
            return render(request, 'pharmacypages/manageMedicine/edit_medicine.html', {'form': form, 'medicine': medicine})
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
        messages.success(request, "Medicine Record deleted successfully.")
        return redirect('manageMedicine')  # Redirect to the managemedicine page

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

    return render(request, 'pharmacypages/manageSuppliers/addSupplier.html', {'form': form, 'all_suppliers': all_suppliers})


@login_required
@pharmacist_required
def add_supplier_success(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_suppliers = AddSupplier.objects.filter(pharmacist=pharmacist_instance)
    # success message
    messages.success(request, 'Record Added Successfully')

    return render(request, 'pharmacypages/manageSuppliers/add_Supplier_success.html', {'all_suppliers': all_suppliers})


@login_required
@pharmacist_required
def edit_supplier(request, supplier_id):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    supplier = get_object_or_404(AddSupplier, id=supplier_id, pharmacist=pharmacist_instance)
    print(f"Supplier Data: {supplier}")

    if request.method == 'POST':
        form = AddSupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            print("Supplier Record saved successfully!")  # for debugging
            return redirect('manageSuppliers')
        else:
            print("Form is not valid!")  # for debugging
            return render(request, 'pharmacypages/manageSuppliers/edit_supplier.html', {'form': form, 'supplier': supplier})
    else:
        form = AddSupplierForm(instance=supplier)

    return render(request, 'pharmacypages/manageSuppliers/edit_supplier.html', {'form': form, 'supplier': supplier})


@login_required
@pharmacist_required
def delete_supplier(request, supplier_id):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    supplier = get_object_or_404(AddSupplier, id=supplier_id, pharmacist=pharmacist_instance)

    if request.method == 'POST':
        # Handle form submission to delete the medicine
        supplier.delete()
        messages.success(request, "Supplier Record deleted successfully.")
        return redirect('manageSuppliers')

    return render(request, 'pharmacypages/manageSuppliers/delete_supplier.html', {'supplier': supplier})



# pharmacist online store views
# associate already registered medicine with an image and update stockcount
@login_required
@pharmacist_required
def online_store(request):
    pharmacist_instance = Pharmacist.objects.get(user=request.user)
    all_medicines = AddMedicine.objects.filter(pharmacist=pharmacist_instance)
    return render(request, 'pharmacypages/onlineStore/displayMedicine.html', {'all_medicines': all_medicines})


@login_required
@pharmacist_required
def associate_image(request, medicine_id):
    medicine = get_object_or_404(AddMedicine, id=medicine_id)

    if request.method == 'POST':
        form = ImageAssociationForm(request.POST, request.FILES, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('associate-image',medicine_id=medicine.id)
    else:
        form = ImageAssociationForm(instance=medicine)

    return render(request, 'pharmacypages/onlineStore/associate_image.html', {'form': form, 'medicine': medicine})


def manage_clients(request):
    pharmacist = request.user.pharmacist
    my_customers = pharmacist.my_customers.all()
    return render(request, 'pharmacypages/manageClients/myClients.html', {'pharmacist': pharmacist, 'my_customers': my_customers})


def reports_view(request):
    # Calculate the required information
    total_medicines = AddMedicine.objects.count()
    total_online_store_medicines = AddMedicine.objects.filter(image__isnull=False).count()
    total_suppliers = AddSupplier.objects.count()
    total_clients = Customer.objects.count()
    active_suppliers = AddSupplier.objects.filter(status='Active').count()

    context = {
        'total_medicines': total_medicines,
        'total_online_store_medicines': total_online_store_medicines,
        'total_suppliers': total_suppliers,
        'total_clients': total_clients,
        'active_suppliers': active_suppliers,
    }

    return render(request, 'pharmacypages/reports.html', context)