from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import riding_call


class CallRidingView(APIView):
    """
    손님이 탑승 완료한 view
    """
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, assign_id: int):
        try:
            response = riding_call(assign_id)
            if response["statusCode"] == 200:
                return Response(response, status=status.HTTP_200_OK)
            elif response["statusCode"] == 404:
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            elif response["statusCode"] == 400:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.ValidationError:
             return Response({"statusCode":400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)