# Generated by Django 2.2.1 on 2019-11-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.FileField(upload_to='uploads/checkers')),
            ],
            options={
                'verbose_name_plural': 'Checkers',
                'verbose_name': 'Checker',
            },
        ),
    ]
