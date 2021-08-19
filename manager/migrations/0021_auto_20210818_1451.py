# Generated by Django 3.2.6 on 2021-08-18 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_qvant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='name',
            new_name='user',
        ),
        migrations.AddField(
            model_name='claim',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qvant',
            name='cours',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.course'),
        ),
    ]