from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


# =========================
# الصفحة الرئيسية
# =========================
def home(request):
    """
    الصفحة الرئيسية للموقع
    """
    return render(request, "home.html")


urlpatterns = [
    # الصفحة الرئيسية (اسمها home ← مهم)
    path("", home, name="home"),

    # لوحة التحكم
    path("admin/", admin.site.urls),

    # التطبيقات
    path("catalog/", include("catalog.urls")),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
]


# =========================
# ملفات الميديا أثناء التطوير
# =========================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
