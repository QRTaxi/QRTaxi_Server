from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import *

class ReceiveAcceptView(APIView):
    """
    기사님이 수락 요청하는 view
    """
    def post(self, request, *args, **kwargs):
        try:
            response = get_accept_status(request.data)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
            return Response({"statusCode": 400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)