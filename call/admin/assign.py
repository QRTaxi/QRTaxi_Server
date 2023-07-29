from django.contrib import admin
from call.models import Assign


@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    """Admin View for Assign"""

    list_display = (
        "qr_id",
        "driver_id",
        "status",
    )