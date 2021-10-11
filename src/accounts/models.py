from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """
    A model that represents a user
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, null=False, blank=False)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    def __str__(self):
        return self.username


class Contributor(models.Model):
    """
    A model that represents a contributor to a project
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    permission = models.CharField(max_length=20, choices=(), null=True)
    role = models.CharField(max_length=20, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "project"], name="unique-contributor")]

    def __str__(self):
        return self.user
