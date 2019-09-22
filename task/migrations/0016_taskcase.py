# Generated by Django 2.2.5 on 2019-09-22 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_theme_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Theme')),
            ],
            options={
                'verbose_name': 'TaskCase',
                'verbose_name_plural': 'TasksCase',
            },
        ),
    ]
