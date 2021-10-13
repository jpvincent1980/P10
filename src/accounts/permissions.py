from rest_framework.permissions import BasePermission

from accounts.models import Contributor
from projects.models import Project


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
        contributors = Contributor.objects.filter(project=view.kwargs.get(look_for, None))
        author_id = Project.objects.get(pk=view.kwargs.get(look_for,None)).author_user_id.pk
        contributors_ids = [contributor.user_id for contributor in
                            contributors]
        if author_id:
            contributors_ids.append(author_id)
            return request.user.pk in contributors_ids
        return False


class IsAuthor(BasePermission):
    """
    Custom permission to allow author of a project/issue/comment to update and
    delete their own project/issue/comment
    """
    def has_object_permission(self, request, view, obj):
        if view.kwargs.get("pk", None):
            # First condition handles all URI except /projects/{id}/users/{id}
            if hasattr(obj,"author_user_id"):
                return obj.author_user_id == request.user
            # Second condition handles /projects/{id}/users/{id} URI
            elif view.kwargs.get("project_pk", None):
                project = Project.objects.get(pk=view.kwargs.get("project_pk"))
                return project.author_user_id == request.user
        return False
