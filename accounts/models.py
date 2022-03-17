from django.db import models, transaction
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password
        """
        if not email:
            raise ValueError("Merci de renseigner une adresse email.")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.username = user.email
                user.set_password(password)
                user.save(using=self._db)
                return user
        except (ValueError, AttributeError):
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    A model that represents a user with admin-compliant permissions
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contributor(models.Model):
    """
    A model that represents a contributor to a project
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    permission = models.CharField(max_length=20, choices=(), null=True)
    role = models.CharField(max_length=20, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "project"],
                                               name="unique-contributor")]

    def __str__(self):
        return self.user
