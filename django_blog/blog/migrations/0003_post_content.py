# Generated by Django 5.0.8 on 2024-09-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
