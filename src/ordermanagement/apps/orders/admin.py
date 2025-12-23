from django.contrib import admin
from apps.core.admin import CustomModelAdmin
from apps.orders.models import Orders

# Register your models here.


class OrderAdmin(CustomModelAdmin):
    """OrderAdmin"""

    list_display = (
        "order_number",
        "middelware_verified",
        "shopware_verified",
        "quivers_verified",
    )
    search_fields = ("order_number",)
    list_filter = ("is_active", "created_at", "modified_at")


admin.site.register(Orders, OrderAdmin)
