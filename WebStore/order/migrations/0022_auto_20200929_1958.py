# Generated by Django 3.1 on 2020-09-29 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20200913_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='time_limit_expire',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 11, 58, 8, 5062, tzinfo=utc), verbose_name='截止有效時間'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='time_limit_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 11, 58, 8, 5031, tzinfo=utc), verbose_name='開始有效時間'),
        ),
    ]
