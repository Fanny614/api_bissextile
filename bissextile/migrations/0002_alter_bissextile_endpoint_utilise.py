# Generated by Django 5.1.3 on 2024-12-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bissextile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bissextile',
            name='endpoint_utilise',
            field=models.CharField(max_length=100),
        ),
    ]