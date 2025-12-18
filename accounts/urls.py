from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
)

app_name = "accounts"

urlpatterns = [
    # =========================
    # Authentication
    # =========================

    # إنشاء حساب
    path("register/", register_view, name="register"),

    # تسجيل الدخول
    path("login/", login_view, name="login"),

    # تسجيل الخروج
    path("logout/", logout_view, name="logout"),
]
