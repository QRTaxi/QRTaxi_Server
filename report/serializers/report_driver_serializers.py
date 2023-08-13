from rest_framework import serializers
from report.models.report_driver import ReportDriver

class ReportDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDriver
        fields = '__all__'