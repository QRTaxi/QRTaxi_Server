from django.contrib import admin
from report.models import ReportUser


@admin.register(ReportUser)
class ReportUserAdmin(admin.ModelAdmin):
    """Admin View for ReportUser"""

    list_display = (
        "driver_id",
        "assign_id",
    )