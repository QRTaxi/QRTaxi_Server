from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from qr.services import create_place

class PlaceView(APIView):
    """
    QR 장소를 만드는 View
    """
    def post(self, request, *args, **kwargs):
        try:
            create_place(request.data)
            return Response({"detail": "QR 장소가 생성되었습니다."}, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
             return Response({"detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
