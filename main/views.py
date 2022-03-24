from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import CustomUser
from .forms import DoctorSignUpForm, PatientSignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


class Home(TemplateView):
    template_name = "home.html"


class SignUpView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class DoctorSignUpView(CreateView):
    model = CustomUser
    form_class = DoctorSignUpForm
    template_name = "registration/signup_form.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        print(username, password)
        return redirect("/")


class PatientSignUpView(CreateView):
    model = CustomUser
    form_class = PatientSignUpForm
    template_name = "registration/signup_form.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        print(username, password)
        return redirect("/")
