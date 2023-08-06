import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings.local')

app = Celery('hackathon')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#테스트할 때만 주석해제하고 실제로 배포할 때는 주석처리하기
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')