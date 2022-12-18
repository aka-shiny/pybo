from django.contrib.auth import views as auth_views
from django.urls import path

from common.views import UserCreateView

app_name = "common"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", UserCreateView.as_view(), name="signup"),
]
