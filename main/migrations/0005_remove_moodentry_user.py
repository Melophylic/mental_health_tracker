# Generated by Django 4.2.16 on 2024-09-18 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_name_moodentry_nama_moodentry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='user',
        ),
    ]
