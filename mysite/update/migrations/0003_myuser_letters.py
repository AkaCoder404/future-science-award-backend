# Generated by Django 4.1.5 on 2023-01-22 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_rename_user_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='letters',
            field=models.FileField(null=True, upload_to='uploads'),
        ),
    ]
