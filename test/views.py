from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .service.test_service import *
from .models import *
from django.shortcuts import render

class TestView(APIView):
    """
    Test용 View
    """
    def get(self, request, *args, **kwargs):
        data = {
            "detail": "test ok"
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = create_post(request)
        return Response(data, status=status.HTTP_200_OK)

def liveblog_index(request, post_pk):
    return render(request, "example.html", {
        "post_pk": post_pk,
    })
