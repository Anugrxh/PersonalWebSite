# Generated by Django 4.2.4 on 2023-11-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_resumedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files')),
            ],
        ),
        migrations.DeleteModel(
            name='resumedb',
        ),
    ]
