from django.urls import path
from Pharmacy import views

urlpatterns = [
    # manage Medicine Urls
    path('pharmacist/manageMedicine', views.manage_medicine, name="manageMedicine"),
    path('pharmacist/manageMedicine/addMedicine', views.add_medicine, name="addMedicine"),
    path('manageMedicine/addMedicine_Success', views.add_medicine_success, name="add_medicine_success"),
    path('edit_medicine/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),

    # pharmacist dashboard Urls
    path('pharmacist/dashboard', views.pharmacist_dashboard, name="dashboard"),

    # manage Suppliers Urls
    path('pharmacist/manageSuppliers', views.manage_suppliers, name="manageSuppliers"),
    path('pharmacist/manageSuppliers/addSupplier', views.add_supplier, name="add_supplier"),
    path('manageSuppliers/addSupplier_Success', views.add_supplier_success, name="add_supplier_success"),

]