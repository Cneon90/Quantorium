# Generated by Django 3.2.6 on 2021-08-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0031_timetable_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='day_work',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='name',
        ),
        migrations.AddField(
            model_name='timetable',
            name='name',
            field=models.ManyToManyField(to='manager.Group'),
        ),
    ]
