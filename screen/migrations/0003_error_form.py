# Generated by Django 5.0.4 on 2024-05-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen", "0002_elementsxpaths"),
    ]

    operations = [
        migrations.CreateModel(
            name="Error_form",
            fields=[
                ("id_error", models.AutoField(primary_key=True, serialize=False)),
                ("date_log_error", models.DateTimeField()),
                ("email_error", models.EmailField(max_length=254)),
                ("comment_error", models.CharField(max_length=500)),
                ("image_error", models.CharField(max_length=200)),
            ],
        ),
    ]