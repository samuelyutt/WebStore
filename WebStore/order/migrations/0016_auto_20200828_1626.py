# Generated by Django 3.1 on 2020-08-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20200826_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='discount_limit_type',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='time_limit_type',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='total_amount_limit_type',
        ),
        migrations.AddField(
            model_name='promo',
            name='has_time_limit',
            field=models.IntegerField(choices=[(0, '無'), (1, '有')], default=0, verbose_name='使用時間限制'),
        ),
        migrations.AddField(
            model_name='promo',
            name='has_total_amount_limit',
            field=models.IntegerField(choices=[(0, '無'), (1, '有')], default=0, verbose_name='消費滿額才可用'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='total_amount_limit',
            field=models.IntegerField(default=0, verbose_name='消費滿此金額可用'),
        ),
    ]
