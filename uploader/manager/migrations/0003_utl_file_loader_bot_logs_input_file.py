# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-13 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_utl_file_loader_bot_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='utl_file_loader_bot_logs',
            name='input_file',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
