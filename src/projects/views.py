from itertools import chain

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsAuthor, IsContributor
from .models import Project, Issue, Comment
from accounts.models import Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from accounts.serializers import ContributorSerializer


# Create your views here.
class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ("list", "create"):
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("retrieve", "update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        if self.action in ("list", "create"):
            author_projects = Project.objects.filter(author_user_id=self.request.user)
            contributor_projects = Project.objects.filter(contributors=self.request.user)
            user_projects = chain(author_projects, contributor_projects)
        else:
            user_projects = Project.objects.all()
        return user_projects


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_permissions(self):
        if self.action in ("list",):
            self.permission_classes = [IsAuthenticated, IsContributor|IsAuthor]
        elif self.action in ("create", "retrieve", "update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_permissions(self):
        if self.action in ("list", "create"):
            self.permission_classes = [IsAuthenticated, IsContributor|IsAuthor]
        elif self.action in ("retrieve", "update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["project_pk"])


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ("list", "create"):
            self.permission_classes = [IsAuthenticated, IsContributor|IsAuthor]
        elif self.action in ("retrieve", "update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs["issue_pk"])
