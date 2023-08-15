from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import get_push_token


class CallPushTokenView(APIView):
    """
    Push Token을 받아오는 View
    """
    def post(self, request):
        try:
            response = get_push_token(request.data)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)