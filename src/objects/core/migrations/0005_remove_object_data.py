# Generated by Django 2.2.12 on 2020-09-03 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_move_data_to_record"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="object",
            name="data",
        ),
    ]
