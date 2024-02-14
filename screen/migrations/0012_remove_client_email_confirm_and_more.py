# Generated by Django 4.2.5 on 2024-02-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0011_client_remove_imagetrack_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email_confirm',
        ),
        migrations.AddField(
            model_name='imagetrack',
            name='notify_validate',
            field=models.BooleanField(default=False),
        ),
    ]
