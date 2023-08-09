from django.urls import path
from utils.api.check_hash import CheckHashingApi
app_name = 'utils'

urlpatterns = [
    path('checkhash/', CheckHashingApi.as_view()),
]