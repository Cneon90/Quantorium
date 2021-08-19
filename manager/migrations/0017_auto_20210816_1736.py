# Generated by Django 3.2.6 on 2021-08-16 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0016_claim'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.course'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]