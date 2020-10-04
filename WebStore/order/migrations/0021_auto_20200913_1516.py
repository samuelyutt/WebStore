# Generated by Django 3.1 on 2020-09-13 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20200829_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='time_limit_expire',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 7, 16, 44, 812643, tzinfo=utc), verbose_name='截止有效時間'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='time_limit_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 7, 16, 44, 812611, tzinfo=utc), verbose_name='開始有效時間'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='total_count_limit',
            field=models.IntegerField(default=10, verbose_name='剩餘使用次數'),
        ),
    ]