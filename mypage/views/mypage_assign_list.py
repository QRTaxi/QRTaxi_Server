from rest_framework.generics import ListAPIView
from call.models import Assign
from mypage.serializers.mypage_assign_list_serializers import AssignSerializer
from driver.models import CustomDriver
from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

class DriverAssignmentsView(ListAPIView):
    serializer_class = AssignSerializer
    authentication_classes = [JWTAuthentication]


    def get_queryset(self):
        driver_id = self.kwargs['pk']
        try:
            driver = CustomDriver.objects.get(pk=driver_id)
        except CustomDriver.DoesNotExist:
            raise Http404
        if driver != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return Assign.objects.filter(driver_id=driver)

    def get(self, request, *args, **kwargs):
        response_data = self.list(request, *args, **kwargs).data
        return Response({'statusCode': status.HTTP_200_OK, 'data':response_data})
