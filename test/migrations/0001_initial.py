# Generated by Django 4.2.3 on 2023-07-29 07:12

from django.db import migrations, models
import test.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('waiting', '배정중'), ('success', '배정완료'), ('riding', '탑승완료'), ('finish', '운행종료'), ('cancel', '취소')], default='waiting', max_length=50)),
                ('driver', models.CharField(max_length=5, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(test.mixins.ChannelLayerGroupSendMixin, models.Model),
        ),
    ]