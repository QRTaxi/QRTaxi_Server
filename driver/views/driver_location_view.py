from driver.services import get_driver_location
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView


class UpdateDriverLocationView(APIView):
    """
    택시 기사님 위치 저장하는 View
    """
    def post(self, request, *args, **kwargs):
        try:
            response = get_driver_location(request.data)
            if response['statusCode'] == 500:
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            elif response['statusCode'] == 400:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            elif response['statusCode'] == 200:
                return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return Response({"statusCode":400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
