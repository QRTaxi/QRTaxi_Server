from utils.redis_utils import get_redis_connection

def get_driver_location(data):
    """
    택시 기사님 위치 저장하는 Service
    """
    driver_id = data.get('id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    redis_conn = get_redis_connection()

    if redis_conn is None:
        return {'status': 'ERROR'}

    locations = (latitude, longitude, driver_id)
    redis_conn.geoadd("driver_location", locations)

    return {'status': 'OK'}