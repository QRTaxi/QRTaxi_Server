from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import get_assign


class ReceiveMainView(APIView):
    """
    배정 상세정보를 보여주는 view
    """
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, assign_id: int):
        try:
            response = get_assign(assign_id)
            if response["statusCode"] == 200:
                return Response(response, status=status.HTTP_200_OK)
            if response["statusCode"] == 404:
                return Response(response, status=status.HTTP_404_NOT_FOUND)
        except exceptions.ValidationError:
            return Response({"statusCode":400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)