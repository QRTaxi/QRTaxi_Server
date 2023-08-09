from rest_framework import serializers
from report.models.report_user import ReportUser

class ReportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportUser
        fields = '__all__'