from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator
)
from django.utils import timezone


class BaseModel(models.Model):
    """Abstract base model."""
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# class ExampleModel(models.Model):
#     """
#     Demonstrates fields, relationships, constraints,
#     model options, custom methods, and hooks.
#     """

#     # --------------------------------------------------
#     # 1. PRIMARY KEY
#     # --------------------------------------------------
#     id = models.BigAutoField(primary_key=True)

#     # --------------------------------------------------
#     # 2. BASIC FIELD TYPES
#     # --------------------------------------------------
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     is_active = models.BooleanField(default=True)
#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         validators=[MinValueValidator(0)]
#     )
#     stock = models.IntegerField(default=0)

#     rating = models.FloatField(
#         null=True,
#         blank=True,
#         validators=[MinValueValidator(0), MaxValueValidator(5)]
#     )

#     launch_date = models.DateField(null=True, blank=True)
#     launch_time = models.TimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # --------------------------------------------------
#     # 3. FILE & MEDIA FIELDS
#     # --------------------------------------------------
#     image = models.ImageField(
#         upload_to="products/images/",
#         null=True,
#         blank=True
#     )
#     manual = models.FileField(
#         upload_to="products/manuals/",
#         null=True,
#         blank=True
#     )

#     # --------------------------------------------------
#     # 4. RELATIONSHIP FIELDS
#     # --------------------------------------------------
#     owner = models.ForeignKey(
#         'accounts.User',
#         on_delete=models.CASCADE,
#         related_name="products"
#     )

#     tags = models.ManyToManyField(
#         "Tag",
#         blank=True,
#         related_name="products"
#     )

#     # --------------------------------------------------
#     # 5. FIELD WITH CHOICES
#     # --------------------------------------------------
#     STATUS_DRAFT = "draft"
#     STATUS_PUBLISHED = "published"
#     STATUS_ARCHIVED = "archived"

#     STATUS_CHOICES = (
#         (STATUS_DRAFT, "Draft"),
#         (STATUS_PUBLISHED, "Published"),
#         (STATUS_ARCHIVED, "Archived"),
#     )

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default=STATUS_DRAFT
#     )

#     # --------------------------------------------------
#     # 6. VALIDATORS
#     # --------------------------------------------------
#     sku = models.CharField(
#         max_length=20,
#         unique=True,
#         validators=[
#             RegexValidator(
#                 regex=r"^[A-Z0-9]+$",
#                 message="SKU must be uppercase alphanumeric"
#             )
#         ]
#     )

#     # --------------------------------------------------
#     # 7. DATABASE INDEXES
#     # --------------------------------------------------
#     class Meta:
#         abstract = True

#         db_table = "products"
#         ordering = ["-created_at"]
#         verbose_name = "Product"
#         verbose_name_plural = "Products"

#         indexes = [
#             models.Index(fields=["name"]),
#             models.Index(fields=["status", "is_active"]),
#         ]

#         constraints = [
#             models.UniqueConstraint(
#                 fields=["name", "owner"],
#                 name="unique_product_per_owner"
#             ),
#             models.CheckConstraint(
#                 check=models.Q(price__gte=0),
#                 name="price_positive"
#             ),
#         ]

#     # --------------------------------------------------
#     # 8. STRING REPRESENTATION
#     # --------------------------------------------------
#     def __str__(self):
#         return f"{self.name} ({self.sku})"

#     # --------------------------------------------------
#     # 9. CUSTOM MODEL METHODS
#     # --------------------------------------------------
#     def is_in_stock(self) -> bool:
#         return self.stock > 0

#     def publish(self):
#         self.status = self.STATUS_PUBLISHED
#         self.save(update_fields=["status"])

#     # --------------------------------------------------
#     # 10. CUSTOM SAVE / DELETE
#     # --------------------------------------------------
#     def save(self, *args, **kwargs):
#         if not self.launch_date:
#             self.launch_date = timezone.now().date()
#         super().save(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         # custom cleanup logic
#         super().delete(*args, **kwargs)
