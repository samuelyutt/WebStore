# Generated by Django 3.1 on 2020-08-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_auto_20200824_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='shipping_fee',
            field=models.IntegerField(default=60),
        ),
    ]
