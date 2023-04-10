from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

		# 작성자에 한해, Blog에 대한 수정/삭제 허용
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 인증여부 상관없이 허용 (GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인 (PUT, DELETE)
        return obj.user == request.user