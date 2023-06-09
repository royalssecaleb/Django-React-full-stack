# Generated by Django 4.0.1 on 2022-07-25 20:23

import core.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0006_user_comments_liked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to=core.user.models.user_directory_path
            ),
        ),
    ]
