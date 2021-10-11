from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from projects.views import ProjectViewset, ContributorViewset, IssueViewset, CommentViewset

router = routers.SimpleRouter()
router.register(r"projects", ProjectViewset, basename="projects")

projects_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
projects_router.register(r"users", ContributorViewset, basename="users")

issues_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
issues_router.register(r"issues", IssueViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues", lookup="issue")
comments_router.register(r"comments", CommentViewset, basename="comments")

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include("accounts.urls")),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),
    path('api/', include(comments_router.urls)),
]
