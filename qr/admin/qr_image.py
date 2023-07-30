from django.contrib import admin
from qr.models import QrImage


@admin.register(QrImage)
class QrImageAdmin(admin.ModelAdmin):
    """Admin View for QrImage"""

    list_display = (
        "qr",
        "qr_url",
    )