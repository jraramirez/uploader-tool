# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TmpTransitionBw(models.Model):
    id = models.IntegerField(primary_key=True)
    service_month = models.CharField(max_length=255, blank=True, null=True)
    manager_email = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_email = models.CharField(max_length=255, blank=True, null=True)
    pg_level = models.CharField(max_length=255, blank=True, null=True)
    daily_expected_hours = models.CharField(max_length=255, blank=True, null=True)
    employee_type = models.CharField(max_length=255, blank=True, null=True)
    bill_to_county = models.CharField(max_length=255, blank=True, null=True)
    geography = models.CharField(max_length=255, blank=True, null=True)
    hp_level = models.CharField(max_length=255, blank=True, null=True)
    seat_country_code = models.CharField(max_length=255, blank=True, null=True)
    seat_country = models.CharField(max_length=255, blank=True, null=True)
    wbs = models.CharField(max_length=255, blank=True, null=True)
    wbs_description = models.CharField(max_length=255, blank=True, null=True)
    aa_type = models.CharField(max_length=255, blank=True, null=True)
    attribute = models.CharField(max_length=255, blank=True, null=True)
    attribute_2 = models.CharField(max_length=255, blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    hp_labor_rate = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)
    usd_labor_currency = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)
    hours = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_TRANSITION_BW'
