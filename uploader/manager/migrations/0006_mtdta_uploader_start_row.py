# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_remove_mtdta_uploader_append_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtdta_uploader',
            name='start_row',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
