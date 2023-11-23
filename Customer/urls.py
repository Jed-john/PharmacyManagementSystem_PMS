from django.urls import path

from Customer import views


urlpatterns = [
    path('view-medicines/', views.customer_view_medicines, name='customer_view_medicines'),
    path('pharmacists',views.pharmacist_list, name='pharmacist_list'),
    path('add_pharmacist/', views.add_my_pharmacist, name='add_my_pharmacist'),
    path('medical_information/', views.medical_information, name='medical_information')
]