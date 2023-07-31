from decouple import config
import boto3
from rest_framework import exceptions
import uuid

def upload_to_s3(image_data, command):
    """
    이미지 데이터를 s3에 올리고 url을 얻는 함수
    """
    aws_access_key = config('S3_ACCESS_KEY')
    aws_secret_key = config('S3_SECRET_KEY')
    bucket_name = 'qrtaxi'
    try:
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        random_uuid = uuid.uuid4()
        object_name = f'{command}-{random_uuid}.png'
        key = command + '/' + object_name
        s3.put_object(Body=image_data, Bucket=bucket_name, Key=key, ContentType='jpg')
        url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{key}"
        return url
    except Exception as e:
        raise exceptions.ValidationError(f"s3 업로드에 에러가 발생했습니다.: {str(e)}")
        