from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from driver.serializers import CustomDriverDetailSerializer
from driver.models import CustomDriver
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    마이페이지 (+회원탈퇴)
    """
    queryset = CustomDriver.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ('GET', 'DELETE'):
            return CustomDriverDetailSerializer
        elif self.request.method in ('PUT', 'PATCH'):
            return CustomDriverDetailSerializer

    def get_object(self):
        user_id = self.kwargs['pk']
        if user_id != str(self.request.user.id):
            raise PermissionDenied("권한이 없습니다.")
        try:
            return CustomDriverDetailSerializer.objects.get(pk=user_id)
        except CustomDriverDetailSerializer.DoesNotExist:
            raise Http404
        #obj = super().get_object()
        #if obj != self.request.user:
        #    raise PermissionDenied("You do not have permission to perform this action.")
        #return obj

    # remove swagger_auto_schema decorators if not needed
    def get(self, request, *args, **kwargs):
        """
        마이페이지; 사용자ID가 {id}인 사용자의 상세 정보
        """
        response_data = self.retrieve(request, *args, **kwargs)
        return Response({'statusCode': status.HTTP_200_OK, 'data':response_data})

    def delete(self, request, *args, **kwargs):
        """
        회원탈퇴; 사용자ID가 {id}인 사용자 삭제
        """
        response_data = self.destroy(request, *args, **kwargs).data
        return Response({'statusCode': status.HTTP_204_NO_CONTENT, 'data': response_data})

    def patch(self, request, *args, **kwargs):
        """
        정보수정; 사용자ID가 {id}인 사용자의 정보 수정
        """
        response_data = self.partial_update(request, *args, **kwargs).data
        return Response({'statusCode': status.HTTP_200_OK, 'data': response_data})
