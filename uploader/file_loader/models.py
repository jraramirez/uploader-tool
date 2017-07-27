# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Tempfin005Raw(models.Model):
    id = models.IntegerField(primary_key=True)
    period = models.CharField(db_column='PERIOD', max_length=255)  # Field name made lowercase.
    employee_number = models.CharField(db_column='EMPLOYEE_NUMBER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='EMPLOYEE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supplemental_pay_type = models.CharField(db_column='SUPPLEMENTAL_PAY_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claim_month = models.CharField(db_column='CLAIM_MONTH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claim_date = models.CharField(db_column='CLAIM_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regular_hours = models.CharField(db_column='REGULAR_HOURS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ot_time_in = models.CharField(db_column='OT_TIME_IN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ot_time_out = models.CharField(db_column='OT_TIME_OUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_ot_hours = models.CharField(db_column='TOTAL_OT_HOURS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overtime_time_amt_pay = models.CharField(db_column='OVERTIME_TIME_AMT_PAY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    standby_hours = models.CharField(db_column='STANDBY_HOURS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stndby_amt = models.CharField(db_column='STNDBY_AMT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shift_hours = models.CharField(db_column='SHIFT_HOURS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shift_amt = models.CharField(db_column='SHIFT_AMT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_payout_php = models.CharField(db_column='TOTAL_PAYOUT_PHP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_payout_usd = models.CharField(db_column='TOTAL_PAYOUT_USD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_payout_percent = models.CharField(db_column='TOTAL_PAYOUT_PERCENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prj_customer = models.CharField(db_column='PRJ_CUSTOMER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prj_customer2 = models.CharField(db_column='PRJ_CUSTOMER2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(db_column='PROJECT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project2 = models.CharField(db_column='PROJECT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wbs = models.CharField(db_column='WBS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wbs_description = models.CharField(db_column='WBS_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcl_final = models.CharField(db_column='DCL_FINAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manager_id = models.CharField(db_column='MANAGER_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manager_name = models.CharField(db_column='MANAGER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modified = models.CharField(db_column='MODIFIED', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempfin005raw'


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
        db_table = 'tmp_transition_bw'
