from django.db import models
from apps.core.models import BaseModel


class Orders(BaseModel):
    """
    Orders Model.
    """
    order_number = models.CharField(
        max_length=100,
        null=False,
    )

    shopware_verified = models.BooleanField(default=False)
    quivers_verified = models.BooleanField(default=False)
    middelware_verified = models.BooleanField(default=False)
    order_create_date = models.DateTimeField(null=False)
    payment_details = models.CharField(default="Unknown")
    additional_details = models.JSONField(
        default=dict,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

        indexes = [
            models.Index(fields=["order_number"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.order_number
