from django.urls import path

from Customer import views


urlpatterns = [
    path('view-medicines/', views.customer_view_medicines, name='customer_view_medicines'),

    path('pharmacists',views.pharmacist_list, name='pharmacist_list'),
    path('add_pharmacist/', views.add_my_pharmacist, name='add_my_pharmacist'),
    path('remove_my_pharmacist/', views.remove_my_pharmacist, name='remove_my_pharmacist'),


    path('medical-information/', views.medical_information, name='display_medical_information'),

    path('makepayment', views.makepayment, name='makepayment')

]