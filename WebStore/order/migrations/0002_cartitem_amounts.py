# Generated by Django 3.1 on 2020-08-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='amounts',
            field=models.IntegerField(default=1),
        ),
    ]
