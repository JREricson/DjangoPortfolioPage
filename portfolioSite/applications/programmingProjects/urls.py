from django.urls import path

from . import views

app_name = "programming_projects"


urlpatterns = [
    path("", views.home, name="hometest"),
]
