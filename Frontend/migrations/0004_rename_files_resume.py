# Generated by Django 4.2.4 on 2023-12-21 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_files_delete_resumedb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='files',
            new_name='Resume',
        ),
    ]
