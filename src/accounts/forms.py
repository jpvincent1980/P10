from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class SignupForm(UserCreationForm):
    """
    A custom UserCreationForm for new users to fill in to be able to sign up
    to the application.
    """
    first_name = forms.CharField(max_length=20,
                                 required=False,
                                 label="Prénom")
    last_name = forms.CharField(max_length=20,
                                required=False,
                                label="Nom")
    email = forms.EmailField(error_messages={'unique':"Cet email est déjà utilisé."})
    password1 = forms.CharField(label=_("Mot de passe"))
    password2 = forms.CharField(label=_("Confirmation du mot de passe"))
    error_messages = {
        'password_mismatch': _('Les mots de passe ne sont pas les mêmes.')
    }

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def clean(self):
        """
        A method overriding the default BaseForm clean() method to check that
        password and confirmed password match.
        """
        cleaned_data = super(SignupForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Le mot de passe doit être identique.")
        return cleaned_data

    def is_valid(self):
        """
        A method overriding the default BaseForm is_valid() method.
        """
        valid = super(SignupForm, self).is_valid()
        if valid:
            return True
        else:
            return False
