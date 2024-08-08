# Generated by Django 5.0.4 on 2024-08-08 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0014_imagebasic_alter_error_form_date_log_error_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error_form',
            name='date_log_error',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 11, 29, 15, 54182, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='imagebasic',
            name='url',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='DateTimeTrack',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 11, 29, 15, 53182, tzinfo=datetime.timezone.utc)),
        ),
    ]