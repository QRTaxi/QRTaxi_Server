from driver.models import CustomDriver
from mypage.serializers.mypage_serializers import MypageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class MypageDetailView(APIView):
    """
    사용자의 상세 정보 조회(마이페이지)
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomDriver.objects.get(pk=pk)
        except CustomDriver.DoesNotExist:
            return Http404
    """
    마이페이지 조회
    """
    def get(self, request, format=None):
        driver = CustomDriver.objects.get(username=request.user)
        serializer = MypageSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """
    마이페이지 수정
    """
    def patch(self, request, format=None):
        driver = CustomDriver.objects.get(username=request.user)
        serializer = MypageSerializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'statusCode': status.HTTP_200_OK, 'data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
