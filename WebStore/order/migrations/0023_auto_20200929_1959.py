# Generated by Django 3.1 on 2020-09-29 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20200929_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='time_limit_expire',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='截止有效時間'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='time_limit_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始有效時間'),
        ),
    ]