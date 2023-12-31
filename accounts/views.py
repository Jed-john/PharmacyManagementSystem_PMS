from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views

from Customer.models import MedicalInformation
from Pharmacy.models import AddMedicine
from .decorators import pharmacist_required, customer_required
from .forms import PharmacistSignUpForm, CustomerSignUpForm, LoginForm
from .models import User, Pharmacist


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


class PharmacistSignUpView(CreateView):
    model = User
    form_class = PharmacistSignUpForm
    template_name = 'accountspages/pharmacist_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pharmacist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pharmacist-home')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accountspages/customer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return redirect('customer-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accountspages/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_pharmacist:
                return reverse('pharmacist-home')
            elif user.is_customer:
                return reverse('customer-home')
        else:
            return reverse('login')


# pharmacist home
@login_required
@pharmacist_required
def pharmacist_home(request):
    return render(request, 'accountspages/pharmacist_home.html')


# customer home
@login_required
@customer_required
def customer_home(request):
    customer = request.user.customer
    medical_info, created = MedicalInformation.objects.get_or_create(customer=customer)
    all_pharmacists = Pharmacist.objects.all()
    total_medicines_in_store = AddMedicine.objects.all()

    return render(request, 'accountspages/customer_home.html',
                  {'customer': customer, 'medical_info': medical_info, 'all_pharmacists': all_pharmacists, 'total_medicines_in_store': total_medicines_in_store})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You have been successfully logged out.")
        return response

    def get_next_page(self):
        next_page = super().get_next_page()
        # You can modify the next_page URL here if needed
        return next_page
