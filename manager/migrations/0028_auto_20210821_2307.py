# Generated by Django 3.2.6 on 2021-08-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0027_delete_qvant'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='count_peopl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='data_close',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='data_creat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='day_work',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
