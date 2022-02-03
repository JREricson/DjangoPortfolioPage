from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "programmingprojects",
        include(
            "portfolioSite.applications.programmingProjects.urls",
            namespace="programming_projects",
        ),
    ),
    path("home/", TemplateView.as_view(template_name="home.html")),
]
