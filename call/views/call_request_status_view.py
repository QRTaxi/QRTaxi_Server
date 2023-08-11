from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import response_status


class CallRequestStatusView(APIView):
    """
    소켓이 끊겼을 때, 해당 assign의 status를 조회하여 response 보내주는 view
    """
    def post(self, request):
        try:
            response = response_status(request.data)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
             return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)