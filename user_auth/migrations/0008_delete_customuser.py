# Generated by Django 5.1 on 2024-09-16 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_auth", "0007_customuser_first_name_customuser_groups_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
