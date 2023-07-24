from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include("test.urls")),

]

schema_view = get_schema_view(
    openapi.Info(
        title='제목',
        default_version='API 버전',
        description=
        '''
        API 문서 설명

        작성자 : ...
        ''',
        terms_of_service='',
        contact=openapi.Contact(name='이름', email='이메일'),
        license=openapi.License(name='API 문서 이름')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=urlpatterns,
)

urlpatterns += [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]