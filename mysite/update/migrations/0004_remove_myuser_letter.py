# Generated by Django 4.1.5 on 2023-01-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0003_myuser_letters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='letter',
        ),
    ]