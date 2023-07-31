# Generated by Django 4.2.3 on 2023-07-31 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('assign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.assign', verbose_name='신고당한 배정')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='신고한 기사님')),
            ],
        ),
        migrations.CreateModel(
            name='ReportDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('assign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.assign', verbose_name='신고한 유저')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='신고당한 기사님')),
            ],
        ),
    ]
