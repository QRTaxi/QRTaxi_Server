import qrcode
from qr.serializers import QrImageSerializer
from qr.services import upload_to_s3
from PIL import Image
import json
import requests
import io

def make_qr_image(qr_id):
    """
    qrcode를 생성하는 함수
    """
    thumb_url = "https://qrtaxi.s3.ap-northeast-2.amazonaws.com/logo/qrtaxi_logo.png"
    response = requests.get(thumb_url)
    thumb_img = Image.open(io.BytesIO(response.content))
    thumb_img.thumbnail((200, 200))

    qr = qrcode.QRCode(
        box_size=20,
        border=1
    )

    image_url = "https://qr.com"
    data = {
        "img_url": image_url,
        "location": qr_id
    }
    qr.add_data(json.dumps(data))
    qr.make()

    qr_result = qr.make_image().convert('RGB')
    pos = ((qr_result.size[0] - thumb_img.size[0]) // 2, (qr_result.size[1] - thumb_img.size[1]) // 2)
    qr_result.paste(thumb_img, pos)

    image_data = io.BytesIO()
    qr_result.save(image_data, format='PNG')
    image_data.seek(0)

    result_url = upload_to_s3(image_data.getvalue(), 'qr_image')
    return result_url, image_url


def create_qr_image(create_qr_image_data):
    """
    QR의 장소를 생성하는 Serivice
    """
    qr_id = create_qr_image_data.get('qr')

    qr_image_url, qr_url = make_qr_image(qr_id)
    create_qr_image_data['qr_image'] = qr_image_url
    create_qr_image_data['qr_url'] = qr_url

    qr_image_serializer = QrImageSerializer(data=create_qr_image_data)
    qr_image_serializer.is_valid(raise_exception=True)
    qr_image_serializer.save()