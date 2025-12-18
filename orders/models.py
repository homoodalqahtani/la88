from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from catalog.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name=_("المستخدم"),
    )
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("سلة")
        verbose_name_plural = _("السلال")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"سلة - {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("السلة"),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج"),
    )
    quantity = models.PositiveIntegerField(_("الكمية"), default=1)

    class Meta:
        verbose_name = _("عنصر سلة")
        verbose_name_plural = _("عناصر السلة")

    def __str__(self) -> str:
        return f"{self.product} × {self.quantity}"


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("قيد المعالجة")
        PAID = "paid", _("مدفوع")
        SHIPPED = "shipped", _("تم الشحن")
        COMPLETED = "completed", _("مكتمل")
        CANCELLED = "cancelled", _("ملغي")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("المستخدم"),
    )
    status = models.CharField(
        _("حالة الطلب"),
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    total_price = models.DecimalField(
        _("الإجمالي"),
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"طلب رقم #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("الطلب"),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج"),
    )
    price = models.DecimalField(_("سعر الوحدة"), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_("الكمية"))

    class Meta:
        verbose_name = _("عنصر طلب")
        verbose_name_plural = _("عناصر الطلب")

    def __str__(self) -> str:
        return f"{self.product.name} × {self.quantity}"
