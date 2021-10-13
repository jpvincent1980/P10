from django.urls import path, include

from .views import SignupView, test_view

app_name = "accounts"

urlpatterns = [
    path('test/', test_view, name="test"),
    path('signup/', SignupView.as_view(template_name="accounts/signup.html"), name="signup"),
]