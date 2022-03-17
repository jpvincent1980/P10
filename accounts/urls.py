from django.urls import path
from django.contrib.auth import views

from .views import SignupView

app_name = "accounts"

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
    path('signup/', SignupView.as_view(template_name="accounts/signup.html"),
         name="signup"),
]
