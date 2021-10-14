from django.contrib.auth import views
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import CustomUser


# Create your views here.
def redirection_view(request):
    return redirect("/api/login/")


class LoginView(views.LoginView):

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)


class LogoutView(views.LogoutView):
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
            password = request.POST.get("password1")
            user = CustomUser.objects.create(first_name=request.POST.get("first_name"),
                                             last_name=request.POST.get("last_name"),
                                             email=request.POST.get("email"),
                                             username=request.POST.get("email"),
                                             password=password
                                             )
            user.set_password(password)
            user.save()
            return redirect("projects-list")
        else:
            context = {"form": form}
            return render(request, "accounts/signup.html", context)







