from django.contrib.auth import views
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import CustomUser


# Create your views here.
def redirection_view(request):
    """
    A FBV (Function-Based View) redirecting index page to the login page.
    """
    return redirect("/api/login/")


class SignupView(views.FormView):
    """
    A custom FormView for new users to sign up to the application.
    """
    form_class = SignupForm

    def get_context_data(self, **kwargs):
        """
        A method overriding the default FormView context data.
        """
        form = SignupForm
        context = {"form": form, "next": "/api/projects/"}
        return context

    def post(self, request, *args, **kwargs):
        """
        A method overriding the default FormView post() method.
        """
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
