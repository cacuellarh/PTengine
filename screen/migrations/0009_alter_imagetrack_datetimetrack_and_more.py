# Generated by Django 5.0.4 on 2024-05-17 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0008_alter_imagetrack_datetimetrack_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetrack',
            name='DateTimeTrack',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 16, 36, 49, 688457, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]