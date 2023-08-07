from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from driver.services import change_driver_able


class DriverOperationView(APIView):
    permission_classes=[IsAuthenticated]
    """
    택시 기사님 운행 시작 view
    """
    def post(self, request, *args, **kwargs):
        try:
            response = change_driver_able(request.data, request.user)
            if response["statusCode"] == 200:
                return Response(response, status=status.HTTP_200_OK)
            elif response["statusCode"] == 400:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.ValidationError as e:
            return Response({"statusCode":400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
