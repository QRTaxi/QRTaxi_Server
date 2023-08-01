from hashids import Hashids
from decouple import config

class Hashing():
    """
    url을 hashing 하기 윈한 util
    """
    hash_salt = config('HASH_SALT')
    hashids = Hashids(salt=hash_salt, min_length=10)

    @staticmethod
    def encode(target: int):
        hashed = Hashing.hashids.encode(target)

        return hashed
    
    @staticmethod
    def decode(target: str):
        original = Hashing.hashids.decode(target)
        return original[0]
    
test_hashed = Hashing.encode(1)
print(test_hashed)
print(Hashing.decode(test_hashed))