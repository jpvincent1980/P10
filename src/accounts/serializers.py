from rest_framework.serializers import ModelSerializer

from .models import CustomUser, Contributor


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name"]


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]
