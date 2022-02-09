from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = "main_site"

urlpatterns = [
    path("", views.home, name="main_site_home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="portfolioSite/applications/mainSite/templates/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="portfolioSite/applications/mainSite/templates/logout.html"
        ),
        name="logout",
    ),
]
