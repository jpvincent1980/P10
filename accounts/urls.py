from django.urls import path

from .views import SignupView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignupView.as_view(template_name="accounts/signup.html"),
         name="signup"),
]
