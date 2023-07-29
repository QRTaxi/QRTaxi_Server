from django.contrib import admin
from driver.models import CustomDriver


@admin.register(CustomDriver)
class DriverAdmin(admin.ModelAdmin):
    """Admin View for Driver"""

    list_display = (
        "username",
        "phone_num",
        "taxi_num",
    )

    search_fields = (
        "username",
    )