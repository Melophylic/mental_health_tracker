# Generated by Django 4.2.16 on 2024-09-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_moodentry_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodentry',
            name='kelas',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='moodentry',
            name='name',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='moodentry',
            name='npm',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='feelings',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='mood',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='mood_intensity',
            field=models.IntegerField(default='0'),
        ),
    ]
