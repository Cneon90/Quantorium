# Generated by Django 3.2.6 on 2021-08-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_auto_20210818_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type_cours',
            field=models.CharField(choices=[('1', 'Квантум'), ('2', 'Курс')], max_length=1, null=True),
        ),
    ]
