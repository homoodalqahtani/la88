from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(_("اسم التصنيف"), max_length=150)
    slug = models.SlugField(_("المعرف (Slug)"), unique=True)
    is_active = models.BooleanField(_("نشط"), default=True)
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("التصنيف"),
    )

    name = models.CharField(_("اسم المنتج"), max_length=255)
    slug = models.SlugField(_("المعرف (Slug)"), unique=True)
    description = models.TextField(_("وصف المنتج"))
    price = models.DecimalField(_("السعر"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("المخزون"), default=0)
    is_active = models.BooleanField(_("نشط"), default=True)
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("المنتج"),
    )

    # ✅ Cloudinary فقط – بدون ImageField
    image = CloudinaryField(
        verbose_name=_("الصورة"),
        folder="products",
    )

    is_main = models.BooleanField(_("صورة رئيسية"), default=False)

    class Meta:
        verbose_name = _("صورة منتج")
        verbose_name_plural = _("صور المنتجات")

    def __str__(self) -> str:
        return f"{self.product.name}"
