from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls, name='power'),
    path(
        "",
        include(
            "portfolioSite.applications.mainSite.urls",
            namespace="main_site",
        ),
        name="test_home",
    ),
    path(
        "programmingprojects/",
        include(
            "portfolioSite.applications.programmingProjects.urls",
            namespace="programming_projects",
        ),
    ),
    path(
        "test/",
        include(
            "portfolioSite.applications.testingApp.urls",
            namespace="test",
        ),
    ),
]
