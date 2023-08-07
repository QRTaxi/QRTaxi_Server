from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.views import APIView
from call.services import finish_call


class CallFinishView(APIView):
    """
    손님 하차하는 view
    """
    def post(self, request, assign_id: int):
        try:
            response = finish_call(request.user, assign_id)
            if response["statusCode"] == 200:
                return Response(response, status=status.HTTP_200_OK)
            elif response["statusCode"] == 404:
                return Response(response, status=status.HTTP_404_NOT_FOUND)
        except exceptions.ValidationError:
             return Response({"statusCode":400, "detail": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
