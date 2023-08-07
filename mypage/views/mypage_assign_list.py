from rest_framework.views import APIView
from call.models import Assign
from mypage.serializers.mypage_assign_list_serializers import AssignSerializer
from driver.models import CustomDriver
from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

class DriverAssignmentsView(APIView):
    '''
    기사의 배정 내역 확인하는 view
    '''
    serializer_class = AssignSerializer
    authentication_classes = [JWTAuthentication]

    def get_object(self, pk):
        try:
            return CustomDriver.objects.get(pk=pk)
        except CustomDriver.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        driver = self.get_object(pk)
        if driver != request.user:
            raise PermissionDenied("권한이 없습니다.")
        assignments = Assign.objects.filter(driver_id=driver)
        serializer = AssignSerializer(assignments, many=True)
        return Response({'statusCode': status.HTTP_200_OK, 'data':serializer.data})
