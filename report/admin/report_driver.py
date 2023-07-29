from django.contrib import admin
from report.models import ReportDriver


@admin.register(ReportDriver)
class ReportDriverAdmin(admin.ModelAdmin):
    """Admin View for ReportDriver"""

    list_display = (
        "assign_id",
        "driver_id",
    )