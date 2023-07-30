from django.contrib import admin
from qr.models import Qr


@admin.register(Qr)
class QrAdmin(admin.ModelAdmin):
    """Admin View for Qr"""

    list_display = (
        "place",
        "longitude",
        "latitude",
    )