from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class CustomRegisterView(RegisterView):
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, ValidationError):
            custom_response_data = {
                "statusCode": 400,
                "errors": response.data,
            }
            response.data = custom_response_data

        return response

    def get_response_data(self, user):
        original_data = super().get_response_data(user)
        response_data = {
            "statusCode": 200,
            "data": original_data,
        }
        return response_data

class CustomLoginView(LoginView):
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, ValidationError):
            custom_response_data = {
                "statusCode": 400,
                "errors": response.data,
            }
            response.data = custom_response_data
        return response

    def get_response(self):
        original_response = super().get_response()
        original_data = original_response.data
        response_data = {
            "statusCode": 200,
            "data": original_data,
        }
        return Response(response_data)


class CustomLogoutView(LogoutView):
    def logout(self, request):
        super().logout(request)
        return Response({"statusCode": 200, "message": "성공적으로 로그아웃되었습니다.", 
                         "detail": "Neither cookies or blacklist are enabled, so the token has not been deleted server side. Please make sure the token is deleted client side."})
