from utils.redis_utils import get_redis_connection
from rest_framework import exceptions

def set_push_token_to_redis(assign_id: int, token: str):
    redis_con = get_redis_connection()
    if redis_con is None:
        raise exceptions.ValidationError("레디스에 접속할 수 없습니다.")
    redis_con.set(f"assign:{assign_id}", token)

def get_push_token_from_redis(assign_id: int):
    redis_con = get_redis_connection()
    if redis_con is None:
        raise exceptions.ValidationError("레디스에 접속할 수 없습니다.")
    token = redis_con.get(f"assign:{assign_id}")
    if token is None:
        raise exceptions.NotFound("토큰이 존재하지 않습니다.")
    return token