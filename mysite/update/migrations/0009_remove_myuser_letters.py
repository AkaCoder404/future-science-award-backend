# Generated by Django 4.1.5 on 2023-01-22 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0008_rename_upload_time_myuseruploads_uploadtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='letters',
        ),
    ]
