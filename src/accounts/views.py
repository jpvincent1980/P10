from django.contrib.auth import views, authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import SignupForm
from .models import CustomUser


# Create your views here.
class LoginView(views.LoginView):
    pass


class SignupView(views.FormView):
    form_class = SignupForm

    def get_context_data(self, **kwargs):
        form = SignupForm
        context = {"form": form, "next": "/api/projects/"}
        return context

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create(first_name=request.POST.get("first_name"),
                                             last_name=request.POST.get("last_name"),
                                             email=request.POST.get("email"),
                                             username=request.POST.get("email"),
                                             password=request.POST.get("password1")
                                             )
            return redirect("projects-list")
        else:
            context = {"form": form}
            return render(request, "accounts/signup.html", context)







