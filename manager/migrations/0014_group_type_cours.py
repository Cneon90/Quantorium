# Generated by Django 3.2.6 on 2021-08-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20210816_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='type_cours',
            field=models.CharField(choices=[('R', 'Red'), ('B', 'Yellow'), ('G', 'White')], max_length=1, null=True),
        ),
    ]