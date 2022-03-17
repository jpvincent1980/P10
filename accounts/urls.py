from django.urls import path
from django.contrib.auth import views

from .views import SignupView

app_name = "accounts"

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', SignupView.as_view(template_name="accounts/signup.html"),
         name="signup"),
]
