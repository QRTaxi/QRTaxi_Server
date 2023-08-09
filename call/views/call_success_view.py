from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import get_success_info

class CallSuccessView(APIView):
    """
    택시 호출 성공 후 assign 정보를 보여주는 view
    """
    def get(self, request, hashed_assign_id: str):
        try:
            response = get_success_info(hashed_assign_id)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        