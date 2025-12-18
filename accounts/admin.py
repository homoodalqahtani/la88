from django.contrib import admin
from .models import User, Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone',
        'is_customer',
        'is_admin',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_customer',
        'is_admin',
        'is_staff',
        'is_active',
    )
    search_fields = (
        'username',
        'email',
        'phone',
    )
    ordering = ('username',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'city',
        'district',
        'street',
        'postal_code',
        'created_at',
    )
    list_filter = ('city',)
    search_fields = (
        'user__username',
        'city',
        'district',
    )
