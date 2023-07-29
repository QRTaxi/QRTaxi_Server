# Generated by Django 4.2.3 on 2023-07-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='큐알 장소')),
                ('longitude', models.FloatField(verbose_name='경도')),
                ('latitude', models.FloatField(verbose_name='위도')),
                ('map_image', models.ImageField(upload_to='', verbose_name='장소 이미지')),
            ],
        ),
        migrations.CreateModel(
            name='QrImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_url', models.URLField(max_length=1024)),
                ('qr_image', models.ImageField(upload_to='')),
                ('qr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qr.qr')),
            ],
        ),
    ]
