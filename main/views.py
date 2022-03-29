from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView
from .models import CustomUser
from .forms import DoctorSignUpForm, PatientSignUpForm
from django.contrib.auth import login, authenticate
from blog.models import Post, Category


def home(request):
    if request.user.is_authenticated:
        if request.user.is_doctor:
            return redirect("/doctor")
        elif request.user.is_patient:
            return redirect("/patient")
        else:
            return render(request, "home.html", {})

    else:
        return render(request, "home.html", {})


class DoctorDashBoard(TemplateView):
    model = Post
    template_name = "doctor_dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Post.objects.all().filter(
            written_by=self.request.user, draft=False
        )
        return context


class PostsView(ListView):
    model = Post
    template_name = "patient_dash.html"
    queryset = Post.objects.filter(draft=False).order_by("category")


class PatientDashBoard(TemplateView):
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
        return redirect("/")
