from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import get_main


class CallMainView(APIView):
    """
    웹 택시를 호출하는 메인 View
    """
    def get(self, request, hashed_qr_id: str):
        try:
            response = get_main(hashed_qr_id)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
             return Response({"detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
