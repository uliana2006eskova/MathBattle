# Generated by Django 2.2.5 on 2019-11-09 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20191109_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='finishDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 14, 48, 35, 146838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 14, 48, 35, 146810, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solution',
            name='submitTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 14, 48, 35, 146022, tzinfo=utc)),
        ),
    ]