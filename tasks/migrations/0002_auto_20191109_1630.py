# Generated by Django 2.2.5 on 2019-11-09 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='need_rang',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contest',
            name='finishDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 13, 30, 19, 415997, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 13, 30, 19, 415961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solution',
            name='submitTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 9, 13, 30, 19, 414970, tzinfo=utc)),
        ),
    ]