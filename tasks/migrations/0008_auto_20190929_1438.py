# Generated by Django 2.2.5 on 2019-09-29 11:38

import checker.virdicts
import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import enumfields.fields
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20190929_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='finishDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 29, 11, 38, 19, 779532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 29, 11, 38, 19, 779488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solution',
            name='verdict',
            field=enumfields.fields.EnumField(default='WRONG_ANSWER', enum=checker.virdicts.Virdict, max_length=500),
        ),
        migrations.AlterField(
            model_name='theme',
            name='hardness',
            field=enumfields.fields.EnumField(default='MIDDLE', enum=tasks.models.Hardness, max_length=500),
        ),
    ]