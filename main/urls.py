from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import (
    home,
    DoctorSignUpView,
    PatientSignUpView,
    SignUpView,
    DoctorDashBoard,
    PatientDashBoard,
    PostsView,
    
)

urlpatterns = [
    path("", home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
     path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/doctor/", DoctorSignUpView.as_view(), name="signup_doctor"),
    path("signup/patient/", PatientSignUpView.as_view(), name="signup_patient"),
    path("doctor/", DoctorDashBoard.as_view(), name="doctor"),
    path("patient/", PatientDashBoard.as_view(), name="patient"),
    path("patient/posts/", PostsView.as_view(), name="all_posts"),
]
