# Generated by Django 4.2.3 on 2023-07-31 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=20, verbose_name='손님 전화번호')),
                ('status', models.CharField(choices=[('waiting', '배정중'), ('success', '배정완료'), ('riding', '탑승완료'), ('finish', '운행종료'), ('cancel', '취소')], default='waiting', max_length=10)),
                ('board_at', models.DateTimeField(auto_now=True)),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='기사님')),
                ('qr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.qr', verbose_name='큐알')),
            ],
        ),
    ]
