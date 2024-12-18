# Generated by Django 5.0.4 on 2024-05-16 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0006_alter_imagetrack_datetimetrack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetrack',
            name='frequency_fk',
        ),
        migrations.RemoveField(
            model_name='imagetrack',
            name='rotate',
        ),
        migrations.RemoveField(
            model_name='imagetrack',
            name='scaleX',
        ),
        migrations.RemoveField(
            model_name='imagetrack',
            name='scaleY',
        ),
        migrations.AddField(
            model_name='imagetrack',
            name='ImageTrackDescription',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='DateTimeTrack',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 10, 45, 57, 90154, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Frequency',
        ),
    ]
