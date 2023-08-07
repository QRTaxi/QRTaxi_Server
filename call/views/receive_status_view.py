from call.services import *
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView


class ReceiveStatusView(APIView):
    """
    기사님이 수락 요청하는 view
    """
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            response = get_accept_status(request.data, request.user)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
            return Response({"statusCode": 400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)