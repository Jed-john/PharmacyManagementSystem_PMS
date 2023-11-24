from django.urls import path
from Pharmacy import views

urlpatterns = [
    # manage Medicine Urls
    path('pharmacist/manageMedicine', views.manage_medicine, name="manageMedicine"),
    path('pharmacist/manageMedicine/addMedicine', views.add_medicine, name="addMedicine"),
    path('manageMedicine/addMedicine_Success', views.add_medicine_success, name="add_medicine_success"),
    path('edit_medicine/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),

    # manage Suppliers Urls
    path('pharmacist/manageSuppliers', views.manage_suppliers, name="manageSuppliers"),
    path('pharmacist/manageSuppliers/addSupplier', views.add_supplier, name="add_supplier"),
    path('manageSuppliers/addSupplier_Success', views.add_supplier_success, name="add_supplier_success"),
    path('edit_supplier/<int:supplier_id>/', views.edit_supplier, name='edit_supplier'),
    path('delete_supplier/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),

    # online store urls. List all already added medicines, then option to associate specific medicine with an image to be used for online store in customer side
    path('pharmacist/onlinestore', views.online_store, name="online_store"),
    path('associate-image/<int:medicine_id>/', views.associate_image, name='associate-image'),

    # manage clients urls
    path('pharmacist/manageClients', views.manage_clients, name= 'manageClients'),

    path('reports/', views.reports_view, name='reports'),
]