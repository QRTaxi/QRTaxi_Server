from rest_framework.views import APIView
from call.models import Assign
from mypage.serializers.mypage_assign_list_serializers import AssignSerializer
from driver.models import CustomDriver
from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class DriverAssignmentsView(APIView):
    '''
    기사의 배정 내역 확인하는 view
    '''
    serializer_class = AssignSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        try:
            return CustomDriver.objects.get(username=request.user)
        except CustomDriver.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        driver = CustomDriver.objects.get(username=request.user)
        if driver != request.user:
            return Response({'statusCode': status.HTTP_401_UNAUTHORIZED, 'data':"권한이 없습니다."})
        assignments = Assign.objects.filter(driver_id=driver)
        serializer = AssignSerializer(assignments, many=True)
        return Response({'statusCode': status.HTTP_200_OK, 'data':serializer.data})
