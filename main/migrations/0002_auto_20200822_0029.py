# Generated by Django 3.1 on 2020-08-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lk',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]