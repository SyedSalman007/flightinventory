# Generated by Django 3.2.14 on 2022-07-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='iata',
            field=models.CharField(max_length=3),
        ),
    ]