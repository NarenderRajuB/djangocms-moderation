# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_moderation', '0004_auto_20180614_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemoderationrequestaction',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
