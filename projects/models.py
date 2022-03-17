from django.db import models

from accounts.models import CustomUser, Contributor

TYPES_LIST = [("BACK-END", "Back-End"), ("FRONT-END", "Front-End"), ("IOS", "IOS"), ("ANDROID", "Android")]
TAGS_LIST = [("BUG", "Bug"), ("AMELIORATION", "Amélioration"), ("TACHE", "Tâche")]
PRIORITIES_LIST = [("FAIBLE", "Faible"), ("MOYENNE", "Moyenne"), ("ELEVEE", "Elevée")]
STATUS_LIST = [("A FAIRE", "A faire"), ("EN-COURS", "En-cours"), ("TERMINE", "Terminé")]


# Create your models here.
class Project(models.Model):
    """
    A model that represents a project
    """
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPES_LIST)
    author_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(CustomUser, through=Contributor,
                                          related_name="contributors")

    def __str__(self):
        return self.title


class Issue(models.Model):
    """
    A model that represents an issue
    """
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=20, choices=TAGS_LIST, blank=True,
                           null=True)
    priority = models.CharField(max_length=20, choices=PRIORITIES_LIST,
                                blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_LIST, blank=True,
                              null=True)
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
    author_user_id = models.ForeignKey("accounts.CustomUser",
                                       on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
