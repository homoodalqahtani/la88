from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # الصفحة الرئيسية (واجهة المتجر)
    path('', include('catalog.urls')),

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # التطبيقات الأخرى
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
