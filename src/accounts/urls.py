from .views import LoginView, SignupView
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('signup', SignupView.as_view(template_name="accounts/signup.html"), name="signup"),
]