from rest_framework.permissions import BasePermission

from accounts.models import Contributor
from projects.models import Project, Issue, Comment


class IsContributor(BasePermission):
    """
    Custom permission to allow contributors to a project to create and read
    issues linked to a project, and to create and read comments linked to a
    project
    """
    def has_permission(self, request, view):
        if view.kwargs.get("project_pk", None):
            look_for = "project_pk"
        else:
            look_for = "pk"
        return request.user in Project.objects.get(pk=view.kwargs.get(look_for, None)).contributors.all()


class IsAuthor(BasePermission):
    """
    Custom permission to allow author of a project/issue/comment to update and
    delete their own project/issue/comment
    """
    def has_permission(self, request, view):
        if view.basename == "comments" and view.detail == True:
            return Comment.objects.get(pk=view.kwargs.get("pk",None)).author_user_id.pk == request.user.pk
        elif view.basename == "issues" and view.detail == True:
            return Issue.objects.get(pk=view.kwargs.get("pk",None)).author_user_id.pk == request.user.pk
        elif view.kwargs.get("project_pk", None):
            look_for = "project_pk"
        else:
            look_for = "pk"
        return Project.objects.get(pk=view.kwargs.get(look_for,None)).author_user_id.pk == request.user.pk
