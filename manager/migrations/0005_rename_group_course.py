# Generated by Django 3.2.6 on 2021-08-13 06:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0004_group_news_personal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='group',
            new_name='Course',
        ),
    ]
