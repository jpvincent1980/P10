from rest_framework.serializers import ModelSerializer

from .models import CustomUser, Contributor


class CustomUserSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes CustomUser instances.
    """

    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name"]


class ContributorSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Contributor instances.
    """

    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]
