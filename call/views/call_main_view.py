from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import get_main, post_main


class CallMainView(APIView):
    """
    웹 택시를 호출하는 메인 View
    """
    def get(self, request, hashed_qr_id: str):
        try:
            response = get_main(hashed_qr_id)
            return Response(response, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, hashed_qr_id: str):
        try:
            response = post_main(request.data, hashed_qr_id)
            return Response(response, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
             return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
