from qr.serializers.place_serializer import PlaceSerializer
import requests
import io
from decouple import config
from rest_framework import exceptions
from .s3_service import upload_to_s3

def make_static_map_url(longitude, latitude):
    """
    지정된 좌표가 찍힌 정적 지도를 반환하는 함수
    """
    client_id = config('NCP_CLIENT_ID')
    client_secret = config('NCP_CLIENT_SECRET')

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    url = f"https://naveropenapi.apigw.ntruss.com/map-static/v2/raster?w=400&h=400&markers=type:d|size:mid|pos:{longitude}%20{latitude}"
    try:
        res = requests.get(url, headers=headers)
        image_data = io.BytesIO(res.content)
        result_url = upload_to_s3(image_data, 'static_map')
        return result_url
    except Exception as e:
        raise exceptions.ValidationError(f"지도 생성에 오류가 생겼습니다.: {str(e)}")

def create_place(create_place_data):
    """
    QR의 장소를 생성하는 Serivice
    """
    longitude = create_place_data.get('longitude')
    latitude = create_place_data.get('latitude')

    map_url = make_static_map_url(longitude, latitude)
    create_place_data['map_image'] = map_url
    place_serializer = PlaceSerializer(data=create_place_data)
    place_serializer.is_valid(raise_exception=True)
    place_serializer.save()