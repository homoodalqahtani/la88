from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    مستخدم مخصص (Custom User) قابل للتوسع لاحقًا
    """
    phone = models.CharField(
        _("رقم الجوال"),
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text=_("مثال: 05xxxxxxxx")
    )

    is_customer = models.BooleanField(_("عميل"), default=True)
    is_admin = models.BooleanField(_("مدير متجر"), default=False)

    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")

    def __str__(self) -> str:
        return self.get_username()


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("المستخدم"),
    )

    city = models.CharField(_("المدينة"), max_length=100)
    district = models.CharField(_("الحي"), max_length=100)
    street = models.CharField(_("الشارع"), max_length=255)
    postal_code = models.CharField(_("الرمز البريدي"), max_length=20, blank=True)
    notes = models.TextField(_("ملاحظات"), blank=True)

    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("عنوان")
        verbose_name_plural = _("العناوين")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.city} - {self.district}"
