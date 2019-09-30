# Generated by Django 2.2.5 on 2019-09-30 16:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20190930_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='finishDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 30, 16, 52, 17, 307590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 30, 16, 52, 17, 307555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solution',
            name='submitTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 30, 16, 52, 17, 306668, tzinfo=utc)),
        ),
    ]
