# Generated by Django 3.2.6 on 2021-08-13 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0003_auto_20210810_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('heading', models.CharField(blank=True, max_length=30)),
                ('body', models.TextField()),
                ('data', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_code', models.IntegerField()),
                ('work', models.CharField(blank=True, max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(blank=True, max_length=30)),
                ('g_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
