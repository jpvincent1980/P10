from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.views import ProjectViewset, ContributorViewset, IssueViewset, CommentViewset
from accounts.views import redirection_view

router = routers.SimpleRouter()
router.register(r"projects", ProjectViewset, basename="projects")

projects_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
projects_router.register(r"users", ContributorViewset, basename="users")

issues_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
issues_router.register(r"issues", IssueViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues", lookup="issue")
comments_router.register(r"comments", CommentViewset, basename="comments")

urlpatterns = [
    path('', redirection_view, name="index_redirection"),
    path('api/', include("accounts.urls")),
    path('api/admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),
    path('api/', include(comments_router.urls)),
]
