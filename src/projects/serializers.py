from rest_framework.serializers import ModelSerializer

from .models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Project instances.
    """

    class Meta:
        model = Project
        fields = "__all__"


class IssueSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Issue instances.
    """

    class Meta:
        model = Issue
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Comment instances.
    """

    class Meta:
        model = Comment
        fields = "__all__"
