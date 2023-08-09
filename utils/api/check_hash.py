from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers.check_hashing_serializer import CheckHashingSerializer
from utils import Hashing
from rest_framework import status

class CheckHashingApi(GenericAPIView):
    serializer_class = CheckHashingSerializer

    def post(self, request):
        target = request.data.get('target')
        response = {"target": target}

        if len(target) == 10:
            response["result"] = Hashing.decode(target)
        else:
            response["result"] = Hashing.encode(int(target))
        
        return Response(response, status=status.HTTP_200_OK)
            