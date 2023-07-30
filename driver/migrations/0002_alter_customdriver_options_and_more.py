# Generated by Django 4.2.3 on 2023-07-30 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customdriver',
            options={},
        ),
        migrations.AlterModelManagers(
            name='customdriver',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customdriver',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customdriver',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customdriver',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customdriver',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customdriver',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customdriver',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customdriver',
            name='taxi_num',
            field=models.CharField(error_messages={'unique': '이미 존재하는 차 번호입니다.'}, max_length=20, unique=True, verbose_name='taxi_num'),
        ),
        migrations.AlterField(
            model_name='customdriver',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 존재하는 아이디입니다.'}, max_length=50, unique=True, verbose_name='username'),
        ),
    ]