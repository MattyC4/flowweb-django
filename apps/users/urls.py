from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import signup_view

app_name = "users"

urlpatterns = [
    # tu propia ruta de login primero, para que tenga prioridad
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("", include("django.contrib.auth.urls")),  # logout, password_change, etc.
    path("signup/", signup_view, name="signup"),
]
