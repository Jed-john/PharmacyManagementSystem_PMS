from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),

    path("signup/pharmacist/", views.PharmacistSignUpView.as_view(), name="pharmacist-signup"),
    path("signup/customer/", views.CustomerSignUpView.as_view(), name="customer-signup"),

    path("pharmacist/", views.pharmacist_home, name="pharmacist-home"),
    path("customer/", views.customer_home, name="customer-home"),

    path("login/", views.LoginView.as_view(), name="login"),


    path('logout/', auth_views.LogoutView.as_view(template_name="accountspages/logout.html"), name="logout"),

]