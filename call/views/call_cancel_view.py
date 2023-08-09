from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import cancel_call


class CallCancelView(APIView):
    """
    웹 택시를 취소하는 View
    """ 
    def post(self, request):
        try:
            cancel_call(request.data)
            return Response({"detail": "정상적으로 취소되었습니다."}, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
             return Response({"detail": "잘못된 요청입니다.", "error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
