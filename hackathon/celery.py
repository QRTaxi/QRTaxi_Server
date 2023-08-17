import os
from celery import Celery
import firebase_admin
from firebase_admin import credentials
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings.prod')

app = Celery('hackathon')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

cred_path = config("FIRE_BASE_JSON_KEY_PATH")
cred = credentials.Certificate(cred_path)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

#테스트할 때만 주석해제하고 실제로 배포할 때는 주석처리하기
#@app.task(bind=True, ignore_result=True)
#def debug_task(self):
#    print(f'Request: {self.request!r}')