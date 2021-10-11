from django.db import models

# from accounts.models import CustomUser


# Create your models here.
class Project(models.Model):
    """
    A model that represents a project
    """
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    author_user_id = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Issue(models.Model):
    """
    A model that represents an issue
    """
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=True, null=True)
    author_user_id = models.ForeignKey("accounts.CustomUser",
                                       related_name="author_id",
                                       on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey("accounts.CustomUser",
                                         related_name="assignee_id",
                                         on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """
    A model that represents a comment
    """
    description = models.CharField(max_length=200, blank=True, null=True)
    author_user_id = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
