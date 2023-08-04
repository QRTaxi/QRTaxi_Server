from call.models import Assign
from call.serializers import CallSuccessGetSerializer
from decouple import config
import urllib, json
from rest_framework import exceptions
from redis import Redis
from utils import Hashing
from decouple import config

def get_driver_location(driver_id):
    redis_host = config('REDIS_CACHE_HOST')
    redis_port = config('REDIS_CACHE_PORT')

    redis_con = Redis(host=redis_host, port=redis_port)
    saved_location = redis_con.geopos("driver_location", driver_id)
    result = (saved_location[0][0], saved_location[0][1])
    return result

def change_ms_to_m(milliseconds):
    """
    밀리세컨즈로 나오는 duration 값을 ~분 ~초로 바꿔주는 로직
    """
    seconds = milliseconds // 1000
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}분 {seconds}초"

def calculate_estimated_distance(assign_info):
    """
    현재 기사 위치와 qr 장소의 소요시간을 계산해주는 로직
    """
    client_id = config('NCP_CLIENT_ID')
    client_secret = config('NCP_CLIENT_SECRET')
    
    start = get_driver_location(assign_info.driver_id.id)
    goal = (assign_info.qr_id.longitude, assign_info.qr_id.latitude)

    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}&option=trafast"
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header(f'X-NCP-APIGW-API-KEY', client_secret)
    
    response = urllib.request.urlopen(request)
    res = response.getcode()
    
    if (res == 200) :
        response_body = response.read().decode('utf-8')
        response_body_json = json.loads(response_body)
        result = response_body_json['route']['trafast'][0]['summary']
        duration = change_ms_to_m(result['duration'])
        return duration    
    else:
        raise exceptions.ValidationError("시간 계산을 실패하였습니다.")

def get_success_info(hashed_assign_id: str):
    """
    기사가 배정된 assign 정보를 불러오는 service
    """
    assign_id = Hashing.decode(hashed_assign_id)
    get_assign_info = Assign.objects.select_related('qr_id', 'driver_id').get(id=assign_id)
    if get_assign_info.status == 'success':
        get_assign_serializer = CallSuccessGetSerializer(get_assign_info)
        result = get_assign_serializer.data
        result['estimated_time'] = calculate_estimated_distance(get_assign_info)
        return result
    else:
        raise exceptions.ValidationError("잘못된 운행 상태입니다.")