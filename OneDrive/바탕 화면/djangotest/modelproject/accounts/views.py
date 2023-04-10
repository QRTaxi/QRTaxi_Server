from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from django.contrib.auth.hashers import make_password

# Create your views here.
