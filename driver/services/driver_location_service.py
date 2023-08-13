from utils.redis_utils import get_redis_connection

def get_driver_location(data):
    """
    택시 기사님 위치 저장하는 Service
    """
    driver_id = data.get('driver_id')
    longitude = data.get('longitude')
    latitude = data.get('latitude')
    redis_conn = get_redis_connection(db_select=0)

    if not (-90 <= float(latitude) <= 90) or not (-180 <= float(longitude) <= 180) or not all([driver_id, latitude, longitude]):
        return {'statusCode': 400, 'message': '잘못된 입력값이 있습니다. 모든 필드를 제대로 채웠는지 확인해주세요.'}

    if redis_conn is None:
        return {'statusCode': 500, 'message': '레디스 연결에 실패하셨습니다.'}

    locations = (longitude, latitude, driver_id)
    redis_conn.geoadd("driver_location", locations)

    return {'statusCode': 200}

def get_nearest_drivers(latitude, longitude):
    """
    반경 1km 내에 있는 기사 중 가까운 순으로 10명의 기사 추출하는 Service
    """
    redis_conn = get_redis_connection(db_select=0)

    if not (-90 <= float(latitude) <= 90) or not (-180 <= float(longitude) <= 180) or not all([latitude, longitude]):
        return {'statusCode': 400, 'message': '잘못된 입력값이 있습니다. 모든 필드를 제대로 채웠는지 확인해주세요.'}

    if redis_conn is None:
        return {'statusCode': 500, 'message': '레디스 연결에 실패하셨습니다.'}
    nearest_drivers = redis_conn.georadius('driver_location', longitude, latitude, 1, 'km', withcoord=True, sort='ASC', count=10)

    driver_ids = [int(driver[0].decode('utf-8')) for driver in nearest_drivers]
    return driver_ids