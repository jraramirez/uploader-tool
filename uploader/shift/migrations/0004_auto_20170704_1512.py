# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_auto_20170704_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempfin005raw',
            name='CLAIM_DATE',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='CLAIM_MONTH',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='DCL_FINAL',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='EMPLOYEE_NAME',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='EMPLOYEE_NUMBER',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='MANAGER_ID',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='MANAGER_NAME',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='OT_TIME_IN',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='OT_TIME_OUT',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='OVERTIME_TIME_AMT_PAY',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='PERIOD',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='PRJ_CUSTOMER',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='PRJ_CUSTOMER2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='PROJECT',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='PROJECT2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='SHIFT_AMT',
            field=models.DecimalField(decimal_places=10, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='SHIFT_HOURS',
            field=models.DecimalField(decimal_places=10, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='STANDBY_HOURS',
            field=models.DecimalField(decimal_places=10, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='STNDBY_AMT',
            field=models.DecimalField(decimal_places=10, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='SUPPLEMENTAL_PAY_TYPE',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='tempfin005raw',
            name='WBS',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='CLAIM_DATE',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='CLAIM_MONTH',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='DCL_FINAL',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='EMPLOYEE_NAME',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='EMPLOYEE_NUMBER',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='MANAGER_ID',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='MANAGER_NAME',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='OT_TIME_IN',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='OT_TIME_OUT',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='PERIOD',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='PRJ_CUSTOMER',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='PRJ_CUSTOMER2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='PROJECT',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='PROJECT2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='SUPPLEMENTAL_PAY_TYPE',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='TOTAL_PAYOUT_PERCENT',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='TOTAL_PAYOUT_PHP',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='TOTAL_PAYOUT_USD',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='testfin005raw',
            name='WBS',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
