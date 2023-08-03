from rest_framework.views import APIView
from redis import Redis
from rest_framework.response import Response
from rest_framework import status

# 위치 저장하기 x:latitude(위도) y: longitude(경도)
class UpdateDriverLocationView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        driver_id = data.get('id')
        x = data.get('x')
        y = data.get('y')
        redis_con = Redis(host="redis_cache", port=6380)
        # 위도, 경도, id 순으로
        try:
            if redis_con.ping():
                print("Redis connection is active")
            else:
                print("Failed to connect to Redis")
                return Response({'status': 'ERROR', 'message': 'Failed to connect to Redis'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({'status': 'ERROR', 'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        locations = (x, y, driver_id)
        redis_con.geoadd("driver_location", locations)

        saved_location = redis_con.geopos("driver_location", driver_id)
        if saved_location:
            print(f"Saved location for driver {driver_id}: {saved_location}")
        else:
            print(f"Failed to retrieve location for driver {driver_id}")

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)


class GetNearestDriversView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        x = data.get('x')
        y = data.get('y')

        redis_con = Redis(host="redis_cache", port=6380)

        nearest_drivers = redis_con.georadius('driver_location', x, y, 100, 'km', withdist=True, withcoord=True, sort='ASC', count=5)

        formatted_drivers = [{'driver_id': driver[0].decode('utf-8'), 'distance': driver[1], 'latitude': driver[2][0], 'longitude': driver[2][1]} for driver in nearest_drivers]

        return Response({'nearest_drivers': formatted_drivers}, safe=False, status=200)