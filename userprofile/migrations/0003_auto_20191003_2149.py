# Generated by Django 2.2.5 on 2019-10-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20191003_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='father_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]