# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_mtdta_uploader_append_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtdta_uploader',
            name='append_new',
        ),
    ]
