# Generated by Django 3.1 on 2020-08-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20200829_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.CharField(max_length=32, null=True, verbose_name='優惠代碼'),
        ),
    ]
