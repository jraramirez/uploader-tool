# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mtdta_uploader',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mtdta_uploader_cols',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mtdta_uploader_params',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='mtdta_uploader',
            table='MTDTA_UPLOADER',
        ),
        migrations.AlterModelTable(
            name='mtdta_uploader_cols',
            table='MTDTA_UPLOADER_COLS',
        ),
        migrations.AlterModelTable(
            name='mtdta_uploader_params',
            table='MTDTA_UPLOADER_PARAMS',
        ),
    ]
