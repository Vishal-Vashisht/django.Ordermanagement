from django.conf import settings

# lib imports
from django.contrib import admin
from django.core.cache import cache


class CustomModelAdmin(admin.ModelAdmin):
    """Custom Model Admin"""

    readonly_fields = ("created_at", "modified_at")
    list_per_page = settings.DEFAULT_PAGE_SIZE or 10
    list_max_show_all = 1000

    def has_add_permission(self, request):
        return True if settings.DEBUG else False

    def has_change_permission(self, request, obj=None):
        return True if settings.DEBUG else False

    def has_delete_permission(self, request, obj=None):
        # TODO make it false again later once we found out a way to use shell commands from somewhere
        return True if settings.DEBUG else False

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions["clear_cache"] = (
            self.clear_cache,
            "clear_cache",
            f"Clear Cache for {self.model._meta.verbose_name_plural}",
        )
        return actions

    def clear_cache(self, *args, **kwargs):
        """Clear cache"""
        # TODO: Only clear cache for selected models
        cache.delete_many(cache.keys("*"))
