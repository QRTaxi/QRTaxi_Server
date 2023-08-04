from utils.redis_utils import get_redis_connection

def get_driver_location(data):
    """
    택시 기사님 위치 저장하는 Service
    """
    driver_id = data.get('driver_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    redis_conn = get_redis_connection()

    if not all([driver_id, latitude, longitude]):
        return {'status': 'FIELDERROR', 'message': '잘못된 입력값이 있습니다. 모든 필드를 제대로 채웠는지 확인해주세요.'}

    if redis_conn is None:
        return {'status': 'ERROR', 'message': '레디스 연결에 실패하셨습니다.'}

    locations = (latitude, longitude, driver_id)
    redis_conn.geoadd("driver_location", locations)

    return {'status': 'OK'}