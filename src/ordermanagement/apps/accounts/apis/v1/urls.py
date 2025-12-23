from django.urls import path
from apps.accounts.apis.v1.routers import (
    login
)

urlpatterns = [
    path("auth/login/", login.LoginHandler.as_view(), name="auth-login"),
    path("auth/refresh/", login.RefreshTokenHandler.as_view(), name="auth-refresh")
]
