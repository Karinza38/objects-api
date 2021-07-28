# Generated by Django 2.2.24 on 2021-07-28 14:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("token", "0007_remove_permission_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="permission",
            name="fields",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                help_text="Fields allowed for this token in relation to objecttype versions. Supports only first level of the `record.data` properties",
                null=True,
                verbose_name="mode",
            ),
        ),
    ]
