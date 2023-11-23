from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),

    path("signup/pharmacist/", views.PharmacistSignUpView.as_view(), name="pharmacist-signup"),
    path("signup/customer/", views.CustomerSignUpView.as_view(), name="customer-signup"),

    path("pharmacist/", views.pharmacist_home, name="pharmacist-home"),
    path("customer/", views.customer_home, name="customer-home"),

    path("login/", views.LoginView.as_view(), name="login"),


    path('accountpages/logout.html', CustomLogoutView.as_view(), name='logout'),
]